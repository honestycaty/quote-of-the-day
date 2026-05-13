import json
import random
from datetime import date
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Load quotes from JSON file inside the container
with open("quotes.json", "r") as f:
    quotes = json.load(f)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/quote/random", methods=["GET"])
def random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)


@app.route("/quote/today", methods=["GET"])
def quote_of_the_day():
    # Use today's date to always return the same quote on the same day
    today = date.today()
    index = today.toordinal() % len(quotes)
    quote = quotes[index]
    return jsonify({**quote, "date": str(today)})


@app.route("/quote/<int:quote_id>", methods=["GET"])
def get_quote(quote_id):
    quote = next((q for q in quotes if q["id"] == quote_id), None)
    if not quote:
        return jsonify({"error": f"Quote {quote_id} not found"}), 404
    return jsonify(quote)


@app.route("/quotes", methods=["GET"])
def all_quotes():
    return jsonify({"quotes": quotes, "total": len(quotes)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
