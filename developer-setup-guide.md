# 🛠️ TruthLens Developer Setup Guide

**Complete Installation, Configuration & Development Environment Setup**

---

## 📋 Prerequisites Checklist

### **💻 System Requirements**
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python Version**: Python 3.9 or higher (3.10+ recommended)
- **Memory**: Minimum 4GB RAM (8GB+ recommended for optimal performance)
- **Storage**: At least 2GB free space for dependencies and cache
- **Internet**: Stable internet connection for API services

### **🔧 Required Software**
- **Git**: Version control system for repository management
- **Python**: Latest stable version from [python.org](https://python.org)
- **pip**: Python package manager (included with Python 3.4+)
- **Code Editor**: VS Code, PyCharm, or your preferred Python IDE

### **🔑 API Keys Required**
- **Google Gemini API Key**: For AI content analysis
- **NewsAPI Key**: For news aggregation (free tier available)
- **Google Cloud API Key**: For advanced image analysis (optional)

---

## 🚀 Quick Start Installation

### **Step 1: Clone the Repository**
```bash
# Clone the repository
git clone https://github.com/ssagar0805/MAIN-Streamlitlib-Working-.git

# Navigate to project directory
cd MAIN-Streamlitlib-Working-

# Verify repository contents
ls -la
```

### **Step 2: Create Virtual Environment (Recommended)**
```bash
# Create virtual environment
python -m venv truthlens_env

# Activate virtual environment
# On Windows:
truthlens_env\Scripts\activate

# On macOS/Linux:
source truthlens_env/bin/activate

# Verify activation (should show virtual environment path)
which python
```

### **Step 3: Install Dependencies**
```bash
# Upgrade pip to latest version
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list | grep streamlit
```

### **Step 4: Configure Environment Variables (Optional but Recommended)**
```bash
# Create environment file
touch .env

# Edit .env file with your API keys
# Use your preferred text editor:
nano .env
```

**Environment File Template (`.env`)**:
```env
# Primary AI Services
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_API_KEY=your_google_api_key_here

# News Services
NEWSAPI_KEY=your_newsapi_key_here
NEWSDATA_API_KEY=your_newsdata_key_here

# Firebase Configuration (Optional - for production)
FIREBASE_API_KEY=your_firebase_key
FIREBASE_AUTH_DOMAIN=your_domain.firebaseapp.com
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_STORAGE_BUCKET=your_bucket.appspot.com
FIREBASE_MESSAGING_SENDER_ID=your_sender_id
FIREBASE_APP_ID=your_app_id

# Google Cloud Configuration (Optional)
GOOGLE_CLOUD_PROJECT=your_project_id

# Application Settings
DEBUG=False
APP_NAME=TruthLens
VERSION=2.0.0
```

### **Step 5: Launch Application**
```bash
# Start the Streamlit application
streamlit run app.py

# Application will open automatically in your default browser
# If not, navigate to: http://localhost:8501
```

---

## 🔑 API Key Setup & Configuration

### **🧠 Google Gemini AI Setup**
1. **Visit Google AI Studio**: [https://makersuite.google.com/](https://makersuite.google.com/)
2. **Sign in** with your Google account
3. **Create New API Key**: Click "Get API Key" → "Create API Key"
4. **Copy the API Key** and add to your `.env` file
5. **Test Connection**: The app will verify connectivity on startup

### **📰 NewsAPI Setup**
1. **Visit NewsAPI**: [https://newsapi.org/](https://newsapi.org/)
2. **Register for Free Account**: Sign up with email
3. **Get API Key**: Copy from your dashboard
4. **Free Tier Limits**: 1,000 requests/day (sufficient for development)
5. **Add to Environment**: Set `NEWSAPI_KEY` in `.env` file

### **📊 NewsData.io Setup (Optional Backup)**
1. **Visit NewsData.io**: [https://newsdata.io/](https://newsdata.io/)
2. **Create Account**: Free tier available
3. **Get API Key**: From account dashboard
4. **Set Environment Variable**: `NEWSDATA_API_KEY` in `.env`

### **☁️ Google Cloud Vision (Optional)**
1. **Google Cloud Console**: [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. **Enable Vision API**: Search for "Vision API" and enable
3. **Create Service Account**: IAM & Admin → Service Accounts
4. **Download JSON Key**: Create and download service account key
5. **Set Environment**: `GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json`

---

## 🏗️ Development Environment Setup

### **📝 IDE Configuration**

#### **Visual Studio Code Setup**
```bash
# Install Python extension
code --install-extension ms-python.python

# Install additional helpful extensions
code --install-extension ms-python.black-formatter
code --install-extension ms-python.pylint
code --install-extension ms-toolsai.jupyter
```

**VS Code Settings (`.vscode/settings.json`)**:
```json
{
    "python.defaultInterpreterPath": "./truthlens_env/bin/python",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true
    }
}
```

#### **PyCharm Configuration**
1. **Open Project**: File → Open → Select project directory
2. **Configure Interpreter**: Settings → Project → Python Interpreter
3. **Set Virtual Environment**: Select `truthlens_env/bin/python`
4. **Enable Git Integration**: VCS → Enable Version Control Integration

### **🔧 Development Tools Setup**

#### **Code Formatting & Linting**
```bash
# Install development dependencies
pip install black pylint pytest

# Format code
black .

# Run linting
pylint app.py utils/ pages/

# Run tests (if available)
pytest
```

#### **Git Configuration**
```bash
# Set up Git user (if not already configured)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Check repository status
git status

# Create development branch
git checkout -b development
```

---

## 🌐 Local Development & Testing

### **🚀 Running the Application**

#### **Standard Development Mode**
```bash
# Activate virtual environment
source truthlens_env/bin/activate  # or truthlens_env\Scripts\activate on Windows

# Run with default settings
streamlit run app.py

# Run with specific port
streamlit run app.py --server.port 8502

# Run with debug mode
streamlit run app.py --logger.level debug
```

#### **Development with Auto-reload**
```bash
# Streamlit automatically reloads on file changes
# No additional configuration needed
# Edit files and save - changes will appear immediately
```

### **🔍 Testing Different User Interfaces**

#### **Public User Interface**
- **URL**: `http://localhost:8501`
- **Features**: Text analysis, image analysis, news verification, education
- **Authentication**: None required

#### **Authority Dashboard**
- **URL**: `http://localhost:8501` → Select "Authority Dashboard"
- **Credentials**: 
  - Username: `admin`, Password: `admin123`
  - Username: `officer1`, Password: `secure456`
- **Features**: Live monitoring, investigation tools, advanced analytics

#### **Admin Panel**
- **URL**: `http://localhost:8501?admin=true`
- **Credentials**: Username: `admin`, Password: `truthlens2024`
- **Features**: System administration, user management, email center

### **📊 Testing with Demo Data**
```bash
# Click "Load Demo Data" button in sidebar
# Or programmatically trigger demo data loading
# Demo data includes:
# - Sample analysis results
# - Trending threats
# - User activity simulation
# - System statistics
```

---

## 🧪 Testing & Quality Assurance

### **🔧 Unit Testing Setup**
```bash
# Install testing dependencies
pip install pytest pytest-mock streamlit-testing

# Create test directory structure
mkdir tests
mkdir tests/unit tests/integration

# Run all tests
pytest tests/

# Run with coverage
pytest --cov=. tests/
```

### **🌐 API Testing**
```bash
# Test API connectivity
python -c "
from utils.ai_services import GeminiService
from utils.news_services import NewsAggregator

gemini = GeminiService()
news = NewsAggregator()

print('Gemini API:', gemini.test_connection())
print('News API:', news.test_connection())
"
```

### **🔍 Performance Testing**
```bash
# Monitor application performance
# Use built-in Streamlit profiler
streamlit run app.py --server.enableStaticServing true

# Check memory usage
pip install memory-profiler
python -m memory_profiler app.py
```

---

## 🐛 Troubleshooting Common Issues

### **❌ Installation Issues**

#### **Python Version Errors**
```bash
# Check Python version
python --version

# If version < 3.9, update Python
# Windows: Download from python.org
# macOS: brew install python@3.10
# Ubuntu: sudo apt update && sudo apt install python3.10
```

#### **Dependency Conflicts**
```bash
# Clear pip cache
pip cache purge

# Reinstall dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# Use specific package versions if conflicts persist
pip install streamlit==1.29.0
```

#### **Virtual Environment Issues**
```bash
# Remove existing environment
rm -rf truthlens_env

# Create fresh environment
python -m venv truthlens_env

# Activate and reinstall
source truthlens_env/bin/activate
pip install -r requirements.txt
```

### **🔑 API Key Issues**

#### **Gemini API Errors**
- **Error**: `API key not found`
  - **Solution**: Verify `GEMINI_API_KEY` in `.env` file
  - **Check**: Ensure API key is active in Google AI Studio

- **Error**: `Quota exceeded`
  - **Solution**: Check usage limits in Google AI Studio
  - **Wait**: Rate limits reset daily

#### **News API Errors**
- **Error**: `Invalid API key`
  - **Solution**: Verify `NEWSAPI_KEY` in environment
  - **Check**: Ensure API key is active on newsapi.org

- **Error**: `Rate limit exceeded`
  - **Solution**: Wait for rate limit reset (daily)
  - **Alternative**: Use NewsData.io as backup

### **🚀 Application Launch Issues**

#### **Streamlit Not Starting**
```bash
# Check if streamlit is installed
pip show streamlit

# Reinstall streamlit
pip uninstall streamlit
pip install streamlit==1.29.0

# Try alternative launch method
python -m streamlit run app.py
```

#### **Port Already in Use**
```bash
# Use different port
streamlit run app.py --server.port 8502

# Find and kill process using port 8501
# Windows:
netstat -ano | findstr :8501
taskkill /PID <process_id> /F

# macOS/Linux:
lsof -ti:8501 | xargs kill -9
```

#### **Import Errors**
```bash
# Check if all modules are in path
python -c "import sys; print(sys.path)"

# Verify project structure
ls -la utils/ pages/

# Check for missing __init__.py files
touch utils/__init__.py pages/__init__.py
```

---

## 📁 File Structure for Development

### **🗂️ Project Organization**
```
MAIN-Streamlitlib-Working-/
├── 📄 Development Files
│   ├── app.py                  # Main application entry point
│   ├── config.py               # Configuration management
│   ├── requirements.txt        # Dependencies
│   └── .env                    # Environment variables (create this)
│
├── 📂 Source Code
│   ├── pages/                  # UI components
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── analytics.py
│   │   ├── authority.py
│   │   └── education.py
│   └── utils/                  # Backend services
│       ├── __init__.py
│       ├── ai_services.py
│       ├── database.py
│       ├── email_service.py
│       ├── google_cloud_services.py
│       ├── news_services.py
│       └── security.py
│
├── 📂 Static Assets
│   └── assets/
│       └── styles.css
│
├── 📂 Development Environment
│   ├── truthlens_env/          # Virtual environment (create this)
│   ├── .vscode/                # VS Code settings (optional)
│   └── tests/                  # Test files (create this)
│
└── 📂 Documentation
    ├── README.md files         # Project documentation
    └── ADMIN_ACCESS.md         # Admin access guide
```

---

## 🔄 Development Workflow

### **📝 Daily Development Process**
1. **Activate Environment**: `source truthlens_env/bin/activate`
2. **Pull Latest Changes**: `git pull origin main`
3. **Check Status**: `git status`
4. **Run Application**: `streamlit run app.py`
5. **Make Changes**: Edit code as needed
6. **Test Changes**: Verify functionality in browser
7. **Commit Changes**: `git add .`, `git commit -m "message"`
8. **Push Changes**: `git push origin your-branch`

### **🧪 Testing Checklist**
- [ ] All APIs connecting successfully
- [ ] Text analysis working with sample content
- [ ] Image analysis functioning properly
- [ ] News verification operational
- [ ] Authority dashboard accessible
- [ ] Admin panel loading correctly
- [ ] Email notifications working (if configured)
- [ ] Demo data loading successfully

### **🚀 Pre-deployment Checklist**
- [ ] All environment variables configured
- [ ] API keys valid and active
- [ ] All dependencies installed
- [ ] Code formatted with Black
- [ ] Linting passes without critical errors
- [ ] All features tested manually
- [ ] Performance acceptable
- [ ] No security vulnerabilities
- [ ] Documentation updated

---

## 📚 Additional Resources

### **📖 Documentation**
- **Streamlit Docs**: [https://docs.streamlit.io/](https://docs.streamlit.io/)
- **Google AI Studio**: [https://ai.google.dev/](https://ai.google.dev/)
- **NewsAPI Docs**: [https://newsapi.org/docs](https://newsapi.org/docs)

### **🛠️ Useful Commands**
```bash
# Project management
streamlit --version              # Check Streamlit version
pip freeze > requirements.txt    # Update requirements
pip install --upgrade streamlit  # Update Streamlit

# Development utilities
black --check .                  # Check formatting
pylint app.py                   # Lint main file
pytest -v                       # Verbose testing

# Git workflow
git log --oneline               # View commit history
git branch -a                   # List all branches
git diff                        # Show changes
```

### **🆘 Getting Help**
- **GitHub Issues**: Report bugs and request features
- **Code Comments**: Detailed inline documentation
- **API Documentation**: Check external service docs
- **Community**: Streamlit community forum

---

**Setup Complete!** 🎉 You're ready to develop with TruthLens. The application should be running at `http://localhost:8501` with all features functional.