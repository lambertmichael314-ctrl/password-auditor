document.getElementById('password-input').addEventListener('input', async (e) => {
    const password = e.target.value;

    // Reset UI if input is empty
    if (password.length === 0) {
        updateUI({score: 0, entropy: 0, feedback: []});
        return;
    }

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ password: password })
        });

        const data = await response.json();
        updateUI(data);
    } catch (error) {
        console.error("Error connecting to Python backend:", error);
    }
});

function updateUI(data) {
    const strengthBar = document.getElementById('strength-bar');
    const feedbackList = document.getElementById('feedback');
    const entropyVal = document.getElementById('entropy-value');

    // 1. Update Bar Width based on score (0-6)
    const percentage = (data.score / 6) * 100;
    strengthBar.style.width = percentage + "%";
    
    // 2. Dynamic Color Logic
    // Red for Score 0-2 (Weak), Yellow for 3-4 (Medium), Green for 5-6 (Strong)
    if (data.score <= 2) {
        strengthBar.style.backgroundColor = "#ff4d4d"; // Red
    } else if (data.score <= 4) {
        strengthBar.style.backgroundColor = "#ffd93d"; // Yellow
    } else {
        strengthBar.style.backgroundColor = "#2ecc71"; // Green
    }

    // 3. Update Feedback List
    if (data.feedback.length === 0 && data.score > 0) {
        feedbackList.innerHTML = `<li style="color: #2ecc71;">✓ Password meets all local security criteria.</li>`;
    } else {
        feedbackList.innerHTML = data.feedback.map(f => `<li>${f}</li>`).join('');
    }
    
    // 4. Update Entropy Text and Color
    entropyVal.innerText = `Entropy: ${data.entropy} bits`;
    
    // Highlight entropy in green if it's hit a secure threshold (60+ bits)
    if (data.entropy >= 60) {
        entropyVal.style.color = "#2ecc71";
        entropyVal.style.fontWeight = "bold";
    } else {
        entropyVal.style.color = "#aaa";
        entropyVal.style.fontWeight = "normal";
    }
}