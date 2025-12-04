## 🔗 Kaggle Integration

This project is fully compatible with Kaggle Notebooks. To set up:

1. **Add API Key** (optional for enhanced features):
   - Go to Kaggle Notebook → Add-ons → Secrets
   - Add a new secret named `GEMINI_API_KEY`
   - Paste your Google Gemini API key

2. **Run in Kaggle**:
   ```python
   # Download the project
   github_url = "https://raw.githubusercontent.com/Tethi04/EduMentor-Capstone-Project/main/"
   !curl -L -o agents.py {github_url}agents.py
   !curl -L -o tools.py {github_url}tools.py
   !curl -L -o main.py {github_url}main.py
   
   # Import and use
   from agents import ROOT_AGENT
   response = ROOT_AGENT.assist("Your educational question here")
   print(response)
