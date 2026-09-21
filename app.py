import os
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# Set OPENAI_API_KEY in your environment. Never put the real key in this file.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    question = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()

        if question:
            try:
                response = client.responses.create(
                    model="gpt-4o-mini",
                    input=(
                        "You are an AI Research Assistant. "
                        "Give clear, accurate, beginner-friendly answers. "
                        "When useful, structure the answer with headings and bullet points.\n\n"
                        f"Research question: {question}"
                    )
                )
                answer = response.output_text
            except Exception as e:
                answer = f"Unable to generate a response. Please check your API key and configuration.\n\nError: {e}"
        else:
            answer = "Please enter a research question."

    return render_template("index.html", answer=answer, question=question)


if __name__ == "__main__":
    app.run(debug=True)
