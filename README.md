# AI Research Assistant

An AI-powered research assistant web application built using Python, Flask, HTML, CSS, and OpenAI API integration.

## Features

- Ask research questions through a simple web interface
- Process user questions using a Flask backend
- Generate AI-powered responses using OpenAI API
- Demo Mode available when API credits are unavailable
- Secure API key handling using environment variables
- Simple and responsive web interface

## Technologies

- Python
- Flask
- OpenAI API
- HTML
- CSS

## Project Flow

1. User enters a research question.
2. Flask receives the question from the web interface.
3. The application checks whether an OpenAI API key is available.
4. If the API is available, the question is sent to the OpenAI model.
5. The generated response is displayed on the webpage.
6. If the API is unavailable, the application uses Demo Mode.

## Project Structure

```text
ai-research-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

## Setup

### 1. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
