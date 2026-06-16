import os
import sys
import re
import math
import webbrowser
from threading import Timer
from flask import Flask, render_template, request, jsonify

# --- EXECUTABLE PATH HANDLING ---
# This ensures that when bundled as an EXE, Flask can find the HTML/CSS files
if getattr(sys, 'frozen', False):
    # If the app is running as a bundle (EXE)
    base_path = sys._MEIPASS
    template_folder = os.path.join(base_path, 'templates')
    static_folder = os.path.join(base_path, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    # If the app is running normally via python app.py
    app = Flask(__name__)

# --- STRENGTH ANALYSIS LOGIC ---
def evaluate_strength(password):
    score = 0
    feedback = []

    # 1. Length Check
    length = len(password)
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 chars, 12+ recommended).")

    # 2. Character Diversity
    if re.search(r"[A-Z]", password): 
        score += 1
    else: 
        feedback.append("Missing an uppercase letter.")
    
    if re.search(r"[a-z]", password): 
        score += 1
    
    if re.search(r"\d", password): 
        score += 1
    else: 
        feedback.append("Missing a number.")
    
    if re.search(r"[@$!%*?&]", password): 
        score += 1
    else: 
        feedback.append("Missing a special character (@$!%*?&).")

    # 3. Entropy Calculation (log2(pool^length))
    # Approximation: pool size of 94 for full printable ASCII
    entropy = length * math.log2(94) if length > 0 else 0

    return {
        "score": score, # Max score attainable is 6
        "entropy": round(entropy, 2),
        "feedback": feedback
    }

# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    password = data.get('password', '')
    result = evaluate_strength(password)
    return jsonify(result)

# --- AUTOMATION ---
def open_browser():
    """Opens the local server in the default web browser."""
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Start a timer to open the browser 1 second after the script runs
    # This gives the Flask server time to initialize.
    Timer(1, open_browser).start()
    
    # Run the Flask app
    # debug=False is recommended when building an executable
    app.run(host='127.0.0.1', port=5000, debug=False)
