from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "project": "Lootify AI v2",
        "status": "Running"
    })


@app.route("/generate-post", methods=["POST"])
def generate_post():

    data = request.json

    prompt = f"""

Create a professional Telegram affiliate shopping post.

Product Name:
{data["title"]}

Current Price:
{data["price"]}

Original Price:
{data["original_price"]}

Discount:
{data["discount"]}

Coupon:
{data["coupon"]}

Write a natural human-like Telegram post.

Include:

🔥 Title

50-60 words description

Price

Discount

Coupon

Buy Now👇

"""

    response = model.generate_content(prompt)

    return jsonify({

        "telegram_post": response.text

    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
