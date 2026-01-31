# WhoBot - AI Person Search Web Application

A modern web application that provides AI-generated insights about people using the Groq API and Llama 3.3 model.

## Features

- 🤖 AI-powered person search
- ⚡ Fast responses using Groq API
- 💻 React frontend with beautiful UI
- 🔌 Flask backend API
- 🎨 Responsive design

## Architecture

```
WhoBot/
├── backend/          # Flask REST API
│   ├── app.py       # Main Flask application
│   └── requirements.txt
├── frontend/        # React application
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.jsx
│   └── package.json
└── .env            # Environment variables
```

## Setup

### Prerequisites

- Python 3.9+
- Node.js 16+
- Groq API Key (get it from https://console.groq.com)

### Backend Setup

1. Create virtual environment (if not already created):
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install backend dependencies:
```bash
pip install -r backend/requirements.txt
```

3. Create `.env` file:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

4. Run backend:
```bash
python backend/app.py
```

Backend will run on `http://localhost:5000`

### Frontend Setup

1. Install frontend dependencies:
```bash
cd frontend
npm install
```

2. Start frontend development server:
```bash
npm start
```

Frontend will run on `http://localhost:3000`

## API Endpoints

### GET /

Health check endpoint.

**Response:**
```json
{
  "message": "WhoBot API is running!"
}
```

### POST /api/search

Search for person information.

**Request:**
```json
{
  "name": "Albert Einstein"
}
```

**Response:**
```json
{
  "name": "Albert Einstein",
  "info": "Pioneering theoretical physicist who developed the theory of relativity...",
  "success": true
}
```

## Usage

1. Start the backend server
2. Start the frontend development server
3. Open http://localhost:3000 in your browser
4. Enter a person's name and click "Search"
5. View AI-generated insights about the person

## Technologies Used

- **Backend:** Flask, Flask-CORS, Groq API
- **Frontend:** React, CSS3
- **API:** RESTful API with JSON
- **AI Model:** Llama 3.3 70B (via Groq)

## Security

- API keys are stored in `.env` file (not committed to git)
- `.env` is listed in `.gitignore`
- Use `.env.example` as a template

## License

MIT

## Author

Created for learning and demonstration purposes.
