# 🤖 MyPCOSBuddy Chatbot

This is a lightweight chatbot API built with FastAPI for the **MyPCOSBuddy** application. It helps users interact with PCOS-related content like symptom tracking, diet tips, and lifestyle suggestions.

---

## 🚀 Features

- REST API built using FastAPI
- Simple rule-based chatbot logic (ready for future LLM integration)
- Provides responses to PCOS-related queries
- Clean and extensible structure

---

## 🧑‍💻 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/mypcosbuddy-chatbot.git
cd mypcosbuddy-chatbot

```
### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Chatbot
```bash
uvicorn app.main:app --reload
```
---
## 🛠️ Future Enhancements

🔐 Add authentication using API keys or JWT  
🧠 Integrate OpenAI or Cohere LLM for natural conversation  
📊 Save and track chat history for personalized recommendations  
🌍 Multi-language support  

---

## 🩺 About PCOSBuddy

MyPCOSBuddy is a personal health management platform designed to make life easier for people with PCOS by tracking symptoms, offering lifestyle tips, and using AI to provide personalized insights.

---

