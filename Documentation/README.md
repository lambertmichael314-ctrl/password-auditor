**# Password Strength Auditor (Hybrid Python/JS)**



A standalone security tool that evaluates password cryptographic strength through entropy analysis and pattern verification. It features a real-time JavaScript UI and a Python backend.



**## 📂 Project Structure**

```text

password-auditor/

├── app.py                # Flask Backend (Analysis Logic \& EXE handling)

├── requirements.txt      # Dependencies

├── static/

│   ├── css/style.css     # UI Styling \& Dynamic Transitions

│   └── js/main.js        # Real-time API Interaction \& UI Logic

└── templates/

&nbsp;   └── index.html        # Main Dashboard



**🛠️ Security Features**

Entropy Calculation: Estimates password complexity using the formula $E = L \\cdot \\log\_2(R)$, where $E$ is entropy, $L$ is length, and $R$ is the character pool (set to 94 for standard ASCII).



Heuristic Analysis: Checks for character diversity (uppercase, lowercase, digits, symbols).



Dynamic Visual Feedback: The UI transitions from Red (Weak) to Yellow (Moderate) to Green (Secure) based on the combined security score.

Secure Thresholding: Highlights passwords reaching 60+ bits of entropy as cryptographically strong.



**🚀 Installation \& Setup**



Prepare Environment:

├── python -m venv venv

├── source venv/bin/activate  # Windows: venv\\Scripts\\activate

├── pip install -r requirements.txt



Run Development Server:

├── python app.py

	├── *The tool will automatically open in your default browser at http://127.0.0.1:5000.*



Building the Executable

To package the entire application (including the UI) into a single .exe file:



Windows:

├── pyinstaller --onefile --noconsole --add-data "templates;templates" --add-data "static;static" app.py



macOS/Linux:

├── pyinstaller --onefile --noconsole --add-data "templates:templates" --add-data "static:static" app.py



**## 🔄 Updating the Application**



If you need to change the security logic in Python (app.py) or modify the UI (CSS/JS) after the executable has already been created, follow these steps:



**### 1. Modify the Source Code**

Make your changes to `app.py`, `main.js`, or the styling files. Test your changes locally first by running:

```bash

├── python app.py



**### 2. Clean Up Old Builds**

Before rebuilding, it is best practice to delete the previous build artifacts to prevent conflicts:

*# Delete the temporary folders and the old EXE*

├── rm -rf build/ dist/ app.spec



**### 3. Recompile the Executable**

Run the PyInstaller command again to bundle the updated code into a new EXE:

├── pyinstaller --onefile --noconsole --add-data "templates;templates" --add-data "static;static" app.py



**### 4. Version Control (Recommended)**



**1. Update app.py**

Add the VERSION variable at the top and pass it to the frontend via the index route.



\# ... (at the very top of app.py)

VERSION = "1.1.0"



\# ... (down in the @app.route('/') section)

@app.route('/')

def index():

&nbsp;   # Pass the version variable to the HTML template

&nbsp;   return render\_template('index.html', version=VERSION)



**2. Update templates/index.html**

Add a small version footer or header so you can see it on the screen.



<!-- Add this right above the </div> for the container -->

<div class="version-tag">v{{ version }}</div>



**3. Update static/css/style.css**

Add a bit of styling to keep the version number subtle and professional.



.version-tag {

&nbsp;   font-size: 0.75rem;

&nbsp;   color: #555;

&nbsp;   text-align: center;

&nbsp;   margin-top: 1.5rem;

&nbsp;   font-family: monospace;

}



