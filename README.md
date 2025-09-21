# 🎯 AI-Powered Career & Skills Advisor  

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)  
[![Google AI](https://img.shields.io/badge/Google-Gemini%20AI-yellow?logo=google)](https://ai.google.dev/)  
[![Hackathon](https://img.shields.io/badge/Hackathon-GenAI%202025-green?logo=google-cloud)]()  
[![MIT License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)  

---

## 📌 Overview  

An **AI-powered prototype** that provides **personalized career guidance** for students using **Google Gemini Generative AI**.  
The system analyzes skills, generates career roadmaps, assists with resume writing, and prepares students for interviews.  

Built with **Streamlit** for UI and **Gemini 1.5** for AI-driven insights.  

This project was developed for the **GenAI Hackathon 2025** 🏆.  

---

## ✨ Features  

- 🔍 **Skill Gap Analysis** – Detect missing skills from a student’s profile  
- 🛣️ **Personalized Roadmap** – AI-generated 3-step learning path towards career goals  
- 📄 **Resume Assistance** – Create professional resume highlights with AI suggestions  
- 🎤 **Interview Prep** – Simulated Q&A with concise AI-generated answers  
- ⚡ **Generative AI Core** – Powered by Google’s `gemini-1.5-flash`  

---

## 🛠️ Tech Stack  

- **Frontend:** [Streamlit](https://streamlit.io/)  
- **AI Engine:** [Google Gemini 1.5](https://ai.google.dev/) via `google-generativeai`  
- **Language:** Python 3.9+  
- **Deployment:** Streamlit Cloud  

---

## 🚀 Quick Start  

### 1️⃣ Clone the repo  
```bash
git clone https://github.com/your-username/ai-career-advisor.git
cd ai-career-advisor
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API Key

**Option A – Direct Paste (Quick Hackathon Mode 🚀)**
Edit `app.py`:

```python
genai.configure(api_key="AIza...your_api_key_here...")
```

**Option B – Environment Variable (Secure)**

* **Windows (PowerShell):**

  ```powershell
  setx GOOGLE_API_KEY "AIza...your_api_key_here..."
  ```

* **Linux/Mac:**

  ```bash
  export GOOGLE_API_KEY="AIza...your_api_key_here..."
  ```

### 4️⃣ Run the app

```bash
streamlit run app.py
```

👉 Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌍 Deployment

Easily deploy on **Streamlit Cloud**:

1. Push the project to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy → Share the public link 🎉

---

## ⚡ Hackathon Note

This project was developed during the **GenAI Hackathon 2025**.
It demonstrates how **Generative AI** can transform career guidance and skill development for millions of students in India and beyond.

---
