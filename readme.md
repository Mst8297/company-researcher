# 📘 Company Researcher
AI-powered tool for researching companies using Wikipedia + OpenAI.

## 🚀 Overview
This project lets users enter a company name and instantly get a concise AI-generated analysis.
It uses:
- React Native (Expo) frontend
- FastAPI backend
- Wikipedia API for factual information
- OpenAI for generating the final analysis

The app validates input, checks Wikipedia to ensure the term is actually a company, and returns an informative AI summary.

## 🧱 Architecture

### Frontend (Expo + React Native)
- Clean UI with background image and centered layout
- Enter-key search support
- Displays only the AI response (`openai_response`)
- Handles input validation + friendly error messages

Main files:
app/(tabs)/_layout.tsx
app/(tabs)/index.tsx

### Backend (FastAPI)
Endpoint:
GET /research/{company_name}

Backend flow:
1. Validate input
2. Fetch Wikipedia page
3. Confirm that the page represents a real company
4. Generate summary using OpenAI
5. Return structured JSON

Main files:
backend/app/routers/research.py
backend/app/services/wikipedia.py
backend/app/services/openai_client.py

## 🛠️ Setup

### Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

### Frontend
cd frontend
npm install
npm start

Set EXPO_PUBLIC_API_URL in your environment.

## 📄 License
MIT License
