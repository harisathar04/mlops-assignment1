from flask import request, jsonify
from app import app
from app.model import analyze_sentiment
from flask import render_template


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if "text" not in data or not data["text"].strip():
        return jsonify({"error": "No text provided"}), 400

    sentiment = analyze_sentiment(data["text"])
    return jsonify({"sentiment": sentiment})
