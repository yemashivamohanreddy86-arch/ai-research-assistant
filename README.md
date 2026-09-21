# AI Research Assistant

An AI-powered research assistant built with Python, Flask, and the OpenAI API.

## Features

- Ask research questions through a simple web interface
- Generate AI-powered responses
- Flask backend for handling requests
- Environment variable used for API key security
- Simple HTML/CSS interface

## Technologies

- Python
- Flask
- OpenAI API
- HTML
- CSS

## Project Flow

1. User enters a research question.
2. Flask receives the question.
3. The application sends the question to the OpenAI API.
4. The AI generates a response.
5. Flask displays the response on the web page.

## Setup

### 1. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the API key

Create a `.env` file or set the environment variable directly.

Example:

```text
OPENAI_API_KEY=your_actual_api_key
```

Do not upload `.env` or your real API key to GitHub.

### 4. Run the application

```bash
python app.py
```

Open the local address shown in the terminal, usually:

http://127.0.0.1:5000

## Note

This project is intended as a learning/portfolio project. Keep API credentials private and monitor API usage.
