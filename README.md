# 🎓 EduMentor AI - Intelligent Educational Assistant

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/Tethi04/EduMentor-Capstone-Project?style=social)](https://github.com/Tethi04/EduMentor-Capstone-Project/stargazers)
[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-Notebook-blue)](https://www.kaggle.com/code/tethibiswas/edumentor-ai-educational-system)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tethi04/EduMentor-Capstone-Project/blob/main/notebooks/demo.ipynb)

**EduMentor AI** is a sophisticated multi-agent educational system powered by artificial intelligence, designed to provide personalized learning experiences, generate educational content, and assist students and educators in various academic domains.

## 🌟 Features

### 🤖 **Multi-Agent Architecture**
- **ROOT_AGENT**: Primary educational assistant with comprehensive capabilities
- **GeminiAgent**: Advanced AI integration with Google's Gemini API
- **TutorAgent**: Specialized one-on-one tutoring support
- **AssessmentAgent**: Automated student assessment and analytics

### 📚 **Educational Tools**
- Real-time Q&A assistance across multiple subjects
- Automatic lesson plan generation
- Quiz and assignment creator
- Student performance assessment
- Personalized study schedule generator
- Content complexity analyzer

### 🔧 **Technical Capabilities**
- Modular Python architecture
- Kaggle Notebook integration
- Google Gemini API support
- Extensible agent framework
- Comprehensive error handling
- Interactive command-line interface

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (optional, for enhanced features)

### Installation

```bash
# Clone the repository
git clone https://github.com/Tethi04/EduMentor-Capstone-Project.git
cd EduMentor-Capstone-Project

# Install dependencies
pip install -r requirements.txt

# Run the system
python main.py --mode demo
```

### Quick Setup in Kaggle

```python
# One-cell setup in Kaggle
!pip install google-generativeai -q
!curl -L -o agents.py https://raw.githubusercontent.com/Tethi04/EduMentor-Capstone-Project/main/agents.py
!curl -L -o tools.py https://raw.githubusercontent.com/Tethi04/EduMentor-Capstone-Project/main/tools.py
!curl -L -o main.py https://raw.githubusercontent.com/Tethi04/EduMentor-Capstone-Project/main/main.py

# Import and use
from agents import ROOT_AGENT
response = ROOT_AGENT.assist("Explain quantum physics")
print(response)
```

## 📁 Project Structure

```
EduMentor-Capstone-Project/
├── main.py                 # Main application entry point
├── agents.py               # AI agent definitions and logic
├── tools.py                # Educational utility functions
├── requirements.txt        # Python dependencies
├── README.md              # This documentation
├── .gitignore             # Git ignore file
├── setup.py               # Package installation script
└── notebooks/             # Jupyter notebooks for demos
    └── kaggle_demo.ipynb  # Kaggle integration example
```

## 🎯 Usage Examples

### Basic Q&A
```python
from agents import ROOT_AGENT

# Ask educational questions
response = ROOT_AGENT.assist("Explain photosynthesis in simple terms")
print(response)

# Generate educational content
lesson = ROOT_AGENT.generate_content("Machine Learning", "Beginner", "lesson")
print(lesson)
```

### Advanced Features
```python
from agents import GeminiAgent
from tools import generate_quiz, create_lesson_plan

# Use Gemini AI (requires API key)
gemini_agent = GeminiAgent(api_key="your_api_key")
advanced_response = gemini_agent.assist("Explain neural networks")

# Generate educational materials
quiz = generate_quiz("Biology", 5, "multiple_choice")
lesson_plan = create_lesson_plan("Mathematics", "2 hours", "Advanced")
```

### Command Line Interface
```bash
# Run in interactive mode
python main.py --mode interactive

# Run demo mode
python main.py --mode demo

# Single query mode
python main.py --mode test --query "What is artificial intelligence?"
```

## 🔗 Kaggle Integration

EduMentor is fully compatible with Kaggle Notebooks:

1. **Add API Key** (optional):
   - Go to Kaggle Notebook → Add-ons → Secrets
   - Add secret: `GEMINI_API_KEY` = `your_api_key_here`

2. **Run Complete Setup**:
   ```python
   # Complete Kaggle setup
   from kaggle_secrets import UserSecretsClient
   import google.generativeai as genai
   
   # Get API key
   user_secrets = UserSecretsClient()
   api_key = user_secrets.get_secret("GEMINI_API_KEY")
   
   # Configure Gemini
   if api_key:
       genai.configure(api_key=api_key)
   
   # Import EduMentor
   from agents import ROOT_AGENT, GeminiAgent
   
   # Use the system
   root_response = ROOT_AGENT.assist("Your question here")
   gemini_agent = GeminiAgent(api_key=api_key)
   ```

## 🤖 Agent System

### ROOT_AGENT
The primary educational assistant with capabilities including:
- Multi-subject expertise (Math, Science, History, Programming, etc.)
- Real-time educational Q&A
- Content generation (lessons, quizzes, assignments)
- Student assessment and feedback
- Personalized learning recommendations

### Specialized Agents
- **GeminiAgent**: Enhanced AI capabilities via Google Gemini
- **TutorAgent**: One-on-one personalized tutoring
- **AssessmentAgent**: Automated grading and analytics

## 🛠️ Educational Tools

The system includes a comprehensive toolkit:

```python
from tools import (
    educational_tools,          # List of available tools
    format_response,           # Text formatting utility
    calculate_score,           # Assessment scoring
    get_difficulty_level,      # Adaptive difficulty adjustment
    generate_quiz,             # Quiz generator
    create_lesson_plan,        # Lesson plan creator
    analyze_text_complexity,   # Text analysis for education
    create_study_schedule,     # Personalized study plans
    validate_student_response  # Response validation
)
```

## 📊 API Integration

### Google Gemini API
For enhanced AI capabilities, integrate with Google's Gemini:

```python
# Setup Gemini API
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")

# Use with EduMentor
from agents import GeminiAgent
agent = GeminiAgent(api_key="YOUR_API_KEY")
response = agent.assist("Advanced educational query")
```

**Get API Key**: [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🧪 Testing & Development

Run tests to ensure system functionality:

```bash
# Test basic imports
python -c "from agents import ROOT_AGENT; print(f'✅ {ROOT_AGENT.name} loaded')"

# Run comprehensive tests
python -m pytest tests/ -v

# Check system health
python health_check.py
```

## 📈 Performance & Scalability

- **Modular Design**: Easy to extend with new agents and tools
- **Error Handling**: Comprehensive error recovery and fallback mechanisms
- **Caching**: Intelligent response caching for improved performance
- **Scalability**: Can be extended to support multiple students simultaneously

## 🌐 Web Interface (Coming Soon)

```bash
# Start web server
python web_app.py

# Access at: http://localhost:5000
```

## 📚 Educational Applications

### For Students
- Homework assistance across subjects
- Concept explanation and clarification
- Practice questions and quizzes
- Study schedule creation
- Exam preparation support

### For Educators
- Lesson plan generation
- Quiz and assignment creation
- Student performance analytics
- Content difficulty adjustment
- Classroom activity suggestions

### For Institutions
- Scalable tutoring support
- Standardized assessment tools
- Learning analytics dashboard
- Curriculum development assistance

## 🔍 Debugging & Troubleshooting

Common issues and solutions:

1. **Import Errors**: Ensure all files are in the same directory
2. **API Key Issues**: Verify Gemini API key in Kaggle Secrets
3. **Module Not Found**: Install missing packages from requirements.txt
4. **Connection Issues**: Check internet connectivity for API calls

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Setup
```bash
# Clone with development tools
git clone https://github.com/Tethi04/EduMentor-Capstone-Project.git
cd EduMentor-Capstone-Project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini API** for advanced AI capabilities
- **Kaggle Community** for notebook hosting and collaboration
- **Open Source Contributors** for various Python libraries
- **Educational Technology Researchers** for inspiration

## 📞 Support & Contact

Having issues or questions?

- **GitHub Issues**: [Open an Issue](https://github.com/Tethi04/EduMentor-Capstone-Project/issues)
- **Kaggle Discussion**: [Visit Kaggle Notebook](https://www.kaggle.com/code/tethibiswas/edumentor-ai-educational-system)
- **Email**: [Your Email or Contact]

## 🚀 Future Roadmap

- [ ] Web-based user interface
- [ ] Mobile application
- [ ] Additional AI model integrations
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Integration with LMS platforms
- [ ] Voice interaction capabilities
- [ ] Collaborative learning features

---

<div align="center">

### 🌟 **Star this repo if you find it useful!** 🌟

**Built with ❤️ for the future of education**

[![GitHub Follow](https://img.shields.io/github/followers/Tethi04?label=Follow&style=social)](https://github.com/Tethi04)
[![Kaggle](https://img.shields.io/badge/Kaggle-Profile-blue)](https://www.kaggle.com/tethibiswas)

</div>

## 📊 Project Status

![GitHub last commit](https://img.shields.io/github/last-commit/Tethi04/EduMentor-Capstone-Project)
![GitHub repo size](https://img.shields.io/github/repo-size/Tethi04/EduMentor-Capstone-Project)
![GitHub language count](https://img.shields.io/github/languages/count/Tethi04/EduMentor-Capstone-Project)

---

**Note**: This project is actively maintained. For the latest updates, check the [GitHub repository](https://github.com/Tethi04/EduMentor-Capstone-Project).
