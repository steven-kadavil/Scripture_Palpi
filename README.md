# Scripture_Palpi
Python scripts for backend logic and python for raspberry pi

## **Project Overview:**
A Christian AI assistant that processes voice input through a microphone, sends it to AI APIs for processing, and outputs responses through speakers.


### **Repository Structure:**
```
Scripture_Palpi/
├── flask_app/                 # Flask web server
│   ├── __init__.py
│   ├── routes/
│   │   ├── ai_control.py     # Control AI service
│   │   ├── wifi.py           # WiFi setup
│   │   └── status.py         # Get status
│   └── services/
│       └── ai_manager.py     # Manages AI service
├── ai_service/               # Core AI components
│   ├── voice_recognition.py  # Speech-to-text + wake word
│   ├── ai_integration.py     # AI API integration
│   └── audio_output.py       # Text-to-speech
├── main.py                   # Single entry point (Flask + AI)
└── requirements.txt          # Dependencies
```


### **How to Start:**
```bash
python main.py
```

**This starts both:**
- **Flask server** (port 5000) - for React Native control
- **AI service** (background) - for voice assistant

## **Development Phases:**

### **Phase 1: Core AI Pipeline** ⭐ **START HERE**
- **Voice recognition** - Convert microphone input to text
- **Wake word detection** - "Hey Scripture Palpi"
- **AI model integration** - Send text to ChatGPT/Claude APIs
- **Audio output** - Convert AI response to speech

### **Phase 2: WiFi Setup System**
- **WiFi hotspot creation** - For initial device configuration
- **Web server for configuration** - React Native app communication
- **Credential management** - Store and manage WiFi settings

### **Phase 3: User Memory & Enhancement**
- **Conversation storage** - Database for chat history
- **User preferences** - Customizable AI responses
- **Session management** - Multi-user support

## **Getting Started:**



## ** My Recommendation: Hybrid Approach**

I think the **best solution** is a **hybrid approach**:

```
┌─────────────────┐    HTTP API    ┌─────────────────┐
│   React Native  │ ←────────────→ │   Flask Server  │
│      App        │                │  (Control API)  │
└─────────────────┘                └─────────────────┘
                                           │
                                           ▼
                                    ┌─────────────────┐
                                    │  AI Service     │
                                    │  (Background)   │
                                    └─────────────────┘
                                           │
                                           ▼
                                    ┌─────────────────┐
                                    │ Microphone/     │
                                    │ Speaker         │
                                    └─────────────────┘
```

### **How It Works:**

1. **Flask Server** - Handles React Native communication
2. **AI Service** - Runs as a background process
3. **Communication** - Flask controls the AI service via local API calls

### **Benefits:**
- ✅ **React Native integration** - Full app control
- ✅ **Efficient** - AI service runs directly with hardware
- ✅ **Configurable** - Change settings from your phone
- ✅ **Scalable** - Easy to add features later
