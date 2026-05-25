
# Public API Explorer — Crypto Prices in ₹

A full-stack app that fetches live cryptocurrency prices in INR using the CoinGecko API.

---

## Project Structure
```
public-api-explorer/
├── backend/
│   ├── main.py
│   ├── services.py
│   ├── schemas.py
│   ├── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── Card.jsx
    │   │   └── SearchBar.jsx
    │   ├── services/
    │   │   └── api.js
    │   ├── App.jsx
    │   ├── main.jsx
    │   └── index.css
    └── package.json
```
---

## Backend Setup

1. Navigate to the backend folder
   cd backend

2. Install dependencies
   pip install -r requirements.txt





5. Start the server
   uvicorn main:app --reload

   API runs at http://localhost:8000
   Swagger docs at http://localhost:8000/docs

---

## Frontend Setup

1. Navigate to the frontend folder
   cd frontend

2. Install dependencies
   npm install

3. Start the dev server
   npm run dev

   App runs at http://localhost:5173

---

## API Endpoints

GET /api/coins — Returns top 50 coins by market cap in INR

---

## Tech Stack

Backend  — FastAPI, Pydantic, Requests, python-dotenv
Frontend — React, Vite, vanilla CSS
Data     — CoinGecko Demo API
