import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENAI_API_KEY")


def generate_demo_response(question):
    return f"""Demo Mode Response

Your question:
{question}

The AI Research Assistant received your question successfully
and processed it using the Flask backend.

In OpenAI API Mode, the application can send this question
to an AI model and return a detailed response.

Technologies used:
- Python
- Flask
- HTML
- CSS
- OpenAI API integration
"""


def generate_ai_response(question):
    client = OpenAI(api_key=API_KEY)

    response = client.responses.create(
        model="gpt-4o-mini",
        input=(
            "You are an AI Research Assistant. "
            "Provide clear and relevant answers to research questions.\n\n"
            f"Question: {question}"
        )
    )

    return response.output_text


@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    question = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()

        if question:
            if API_KEY:
                try:
                    answer = generate_ai_response(question)
                except Exception:
                    answer = generate_demo_response(question)
            else:
                answer = generate_demo_response(question)
        else:
            answer = "Please enter a research question."

    return render_template(
        "index.html",
        answer=answer,
        question=question
    )


if __name__ == "__main__":
    app.run(debug=True)
