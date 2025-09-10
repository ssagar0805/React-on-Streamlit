# 🔍 TruthLens - AI-Powered Misinformation Detection System

**Version:** 2.0.0  
**Platform:** Streamlit Web Application with React Frontend Integration  
**Purpose:** Forensic-level misinformation detection and fact-checking system

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Features](#features)
4. [Installation & Setup](#installation--setup)
5. [Project Structure](#project-structure)
6. [React Frontend Integration](#react-frontend-integration)
7. [Usage Guide](#usage-guide)
8. [Development](#development)
9. [Deployment](#deployment)

---

## 🎯 Project Overview

TruthLens is an advanced AI-powered misinformation detection system designed for both public users and authority personnel. It combines multiple AI services, news aggregation, and forensic analysis techniques to identify and combat misinformation in real-time.

### Key Capabilities:
- **Text Analysis**: Deep forensic analysis of text content for misinformation patterns
- **Image Analysis**: Detection of manipulated or fake images
- **URL Investigation**: Verification of web sources and content authenticity
- **Real-time Processing**: AI-powered analysis with immediate results
- **Authority Dashboard**: Advanced monitoring tools for law enforcement
- **Custom React Landing Page**: Modern, responsive user interface

---

## 🏗️ Architecture

### Frontend-Backend Integration
```
┌─────────────────────────────────────────────────────────────┐
│                    Browser (User Interface)                 │
├─────────────────────────────────────────────────────────────┤
│                    Streamlit Framework                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   Python Pages  │  │  Streamlit      │  │   Utilities  │ │
│  │   - home.py     │  │  Components     │  │   - AI       │ │
│  │   - archive.py  │  │  - Built-in     │  │   - Security │ │
│  │   - learn.py    │  │  - Custom       │  │   - Database │ │
│  │   - authority.py│  │                 │  │   - News     │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
├─────────────────────────────────────────────────────────────┤
│              Custom React Component Integration             │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │             tl_frontend/ (React App)                    │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │               frontend/                             │ │ │
│  │  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐ │ │ │
│  │  │  │     src/    │  │    dist/    │  │  node_modules│ │ │ │
│  │  │  │ - React     │  │ - Built     │  │ - Dependencies│ │ │ │
│  │  │  │ - TypeScript│  │ - Assets    │  │ - Vite       │ │ │ │
│  │  │  │ - Tailwind  │  │ - Bundle    │  │ - Tailwind   │ │ │ │
│  │  │  └─────────────┘  └─────────────┘  └──────────────┘ │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  │  __init__.py (Streamlit Component Wrapper)              │ │
│  └─────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                     Backend Services                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   AI APIs   │  │  Security   │  │   External APIs     │  │
│  │  - Gemini   │  │  Services   │  │  - News Sources     │  │
│  │  - Vision   │  │  - Auth     │  │  - Fact Checkers    │  │
│  │  - Language │  │  - Validate │  │  - Social Platforms │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow:
1. **User Interaction** → React Landing Page (Modern UI)
2. **Authentication** → Streamlit Authentication System
3. **Content Analysis** → AI Services (Gemini, Vision, etc.)
4. **Results Display** → Streamlit Components + React UI Elements
5. **Data Storage** → Firebase/Cloud Storage

---

## ✨ Features

### 🔍 **Analysis Capabilities**
- **Text Forensics**: Detect manipulation patterns, emotional triggers, and misinformation
- **Image Analysis**: AI-powered detection of deepfakes, edited images, and synthetic content
- **URL Investigation**: Source verification, reputation scoring, and cross-referencing
- **Multi-language Support**: Analysis in English, Hindi, Tamil, Telugu, Bengali, Marathi

### 🎨 **User Interface**
- **Modern React Landing Page**: Built with TypeScript, Vite, and Tailwind CSS
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Interactive Components**: Smooth animations and modern UI elements
- **Accessibility**: Screen reader compatible and keyboard navigation

### 🛡️ **Security & Authentication**
- **Dual Access Modes**: Public access and Authority login
- **Input Validation**: Protection against malicious inputs
- **Rate Limiting**: Prevent abuse and ensure fair usage
- **Audit Logging**: Track all analysis requests for monitoring

### 📊 **Authority Features**
- **Real-time Monitoring**: Track misinformation trends
- **Bulk Analysis**: Process multiple items simultaneously
- **Reporting Tools**: Generate comprehensive reports
- **API Access**: Programmatic access for integration

---

## 🚀 Installation & Setup

### Prerequisites
```bash
# Required Software
- Python 3.8+ 
- Node.js 18+
- npm or yarn
```

### Step 1: Clone Repository
```bash
git clone https://github.com/ssagar0805/React-on-Streamlit.git
cd React-on-Streamlit
```

### Step 2: Setup React Frontend
```bash
# Navigate to frontend directory
cd tl_frontend/frontend

# Install dependencies
npm install

# Build the React app
npm run build

# Verify build output
ls -la dist/
```

### Step 3: Setup Python Backend
```bash
# Return to root directory
cd ../../

# Install Python dependencies (essential packages)
pip install streamlit==1.29.0 requests python-dotenv

# Optional: Install additional dependencies as needed
# pip install -r requirements.txt
```

### Step 4: Configure Environment
```bash
# Create Streamlit config (optional)
mkdir -p ~/.streamlit
cat > ~/.streamlit/config.toml << EOF
[browser]
gatherUsageStats = false

[server]
headless = true
enableCORS = false
enableXsrfProtection = false
EOF
```

### Step 5: Launch Application

#### Method A: Direct Launch
```bash
streamlit run app_simple.py --server.port 3001 --server.address 0.0.0.0
```

#### Method B: Using PM2 (Recommended for Production)
```bash
# Install PM2 if not already installed
npm install -g pm2

# Start with PM2
pm2 start ecosystem.config.cjs

# Check status
pm2 list
pm2 logs
```

---

## 📁 Project Structure

```
React-on-Streamlit/
├── 📱 Frontend Integration
│   └── tl_frontend/
│       ├── __init__.py                    # Streamlit component wrapper
│       └── frontend/                      # React application
│           ├── src/                       # React source code
│           │   ├── components/            # React components
│           │   ├── pages/                 # React pages
│           │   ├── App.tsx               # Main React app
│           │   └── main.tsx              # React entry point
│           ├── dist/                      # Built React app (output)
│           │   ├── index.html            # Built HTML
│           │   └── assets/               # Built JS/CSS/images
│           ├── package.json              # Node.js dependencies
│           ├── vite.config.ts           # Vite configuration
│           └── tailwind.config.ts       # Tailwind CSS config
│
├── 🐍 Python Backend
│   ├── app.py                           # Original Streamlit app
│   ├── app_simple.py                    # Simplified test app
│   ├── config.py                        # Configuration settings
│   ├── requirements.txt                 # Python dependencies
│   └── ecosystem.config.cjs             # PM2 configuration
│
├── 📄 Pages
│   ├── pages/
│   │   ├── home.py                      # Main landing page with React component
│   │   ├── archive.py                   # Analysis history
│   │   ├── learn.py                     # Educational content
│   │   └── authority.py                 # Authority dashboard
│
├── 🔧 Utilities
│   └── utils/
│       ├── ai_services.py               # AI service integrations
│       ├── news_services.py             # News aggregation
│       ├── security.py                  # Security services
│       └── database.py                  # Database operations
│
├── 🎨 Assets
│   └── assets/
│       └── styles.css                   # Custom CSS
│
└── 📚 Documentation
    ├── README.md                        # This file
    └── *.md                            # Additional documentation
```

---

## ⚛️ React Frontend Integration

### Architecture Overview
The React frontend is integrated into the Streamlit app using **Streamlit Components**:

1. **React App**: Built with modern tools (Vite, TypeScript, Tailwind CSS)
2. **Build Process**: Compiles to static files in `tl_frontend/frontend/dist/`  
3. **Python Wrapper**: `tl_frontend/__init__.py` exposes React component to Streamlit
4. **Integration**: `pages/home.py` imports and renders the React landing page

### Key Files

#### `tl_frontend/__init__.py`
```python
import streamlit.components.v1 as components
from pathlib import Path

# Locate the build folder
_build_dir = Path(__file__).parent / "frontend" / "dist"

# Declare the component, pointing at the build directory
tl_frontend = components.declare_component(
    name="tl_frontend",
    path=str(_build_dir)
)

def render_landing(**kwargs):
    """Render the custom TruthLens landing page component."""
    return tl_frontend(**kwargs)
```

#### `pages/home.py` (React Integration)
```python
from tl_frontend import render_landing

def show_home():
    # Render React Landing Page Component
    render_landing()
    
    # Continue with Streamlit components...
```

### React Component Features
- **Modern UI**: Built with React 18, TypeScript, and Tailwind CSS
- **Component Library**: Uses shadcn/ui for consistent design system
- **Responsive**: Mobile-first design with responsive breakpoints
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Performance**: Optimized with Vite build system

### Development Workflow

#### Frontend Development
```bash
cd tl_frontend/frontend

# Development mode (with hot reload)
npm run dev

# Build for production
npm run build

# Preview build
npm run preview
```

#### Integration Testing
```bash
# Build React frontend first
cd tl_frontend/frontend && npm run build

# Return to root and test Streamlit app
cd ../../
streamlit run app_simple.py --server.port 3001
```

---

## 📖 Usage Guide

### For Public Users

1. **Access the Application**
   - Open the application URL in your browser
   - You'll see the modern React landing page

2. **Authentication**
   - Click "🚀 Enter App (Test Mode)" for public access
   - No registration required for basic features

3. **Analysis Options**
   - **Text Analysis**: Paste text content for fact-checking
   - **URL Investigation**: Enter URLs for source verification
   - **Image Analysis**: Upload images for manipulation detection

### For Authority Users

1. **Authority Login**
   - Select "👮 Authority Login" on the landing page
   - Enter credentials provided by system administrator
   - Access advanced monitoring and reporting tools

2. **Advanced Features**
   - Bulk analysis capabilities  
   - Real-time monitoring dashboard
   - Comprehensive reporting tools
   - API access for integrations

---

## 🛠️ Development

### Adding New Features

#### Frontend (React)
```bash
# Add new React component
cd tl_frontend/frontend/src/components
# Create new component file
# Import and use in pages

# Rebuild after changes
npm run build
```

#### Backend (Streamlit)
```bash
# Add new Streamlit page
# Create in pages/ directory
# Import in main app.py
```

### Debugging

#### React Component Issues
```bash
# Check browser console for JavaScript errors
# Verify build output exists: tl_frontend/frontend/dist/
# Test React component in isolation: npm run dev
```

#### Streamlit Issues
```bash
# Check PM2 logs: pm2 logs
# Test without React component
# Verify Python dependencies: pip list
```

### Testing

```bash
# Test React build
cd tl_frontend/frontend && npm run build

# Test Python imports
python -c "from tl_frontend import render_landing; print('Success')"

# Test full application
streamlit run app_simple.py --server.port 3001
```

---

## 🚀 Deployment

### Local Development
```bash
# Development mode with hot reload
streamlit run app_simple.py --server.port 3001

# Production mode with PM2
pm2 start ecosystem.config.cjs
```

### Production Deployment

#### Prerequisites
- Server with Python 3.8+ and Node.js 18+
- Domain name (optional)
- SSL certificate (recommended)

#### Steps
```bash
# 1. Clone and setup
git clone https://github.com/ssagar0805/React-on-Streamlit.git
cd React-on-Streamlit

# 2. Build frontend
cd tl_frontend/frontend
npm install && npm run build

# 3. Setup backend
cd ../../
pip install -r requirements.txt

# 4. Configure environment variables
# Set up API keys, database connections, etc.

# 5. Deploy with PM2
pm2 start ecosystem.config.cjs
pm2 save
pm2 startup
```

#### Environment Variables
```bash
# Required environment variables
GOOGLE_API_KEY=your_gemini_api_key
FIREBASE_CONFIG=your_firebase_config
NEWS_API_KEY=your_news_api_key
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly (both React and Streamlit components)
5. Submit a pull request

### Code Standards
- **Python**: Follow PEP 8
- **React/TypeScript**: Use ESLint and Prettier
- **Commits**: Use conventional commit messages
- **Documentation**: Update README.md for significant changes

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙋 Support

For support and questions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation wiki

---

## 🔄 Version History

- **v2.0.0** - React frontend integration, modern UI
- **v1.0.0** - Initial Streamlit application
- **v0.1.0** - MVP with basic features

---

*TruthLens - Empowering truth in the digital age* 🔍✨