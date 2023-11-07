from flask import Flask, jsonify


app = Flask(__name__)

games = [
    {"id": 1, "title": "Fallout: New Vegas", "price_usd": "4000"},
    {"id": 2, "title": "Tomb Raider", "price_usd": "3500"},
    {"id": 3, "title": "Stray", "price_usd": "1000"},
]


@app.route("/games", methods=["GET"])
def list_games():
    return jsonify(games)
