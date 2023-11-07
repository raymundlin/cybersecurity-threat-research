from flask import Flask, jsonify
from flagsmith import Flagsmith
import os

flagsmith = Flagsmith(
    environment_key=os.environ["FLAGSMITH_KEY"],
    enable_local_evaluation=True,
)

app = Flask(__name__)

games = [
    {"id": 1, "title": "Fallout: New Vegas", "price_usd": "4000"},
    {"id": 2, "title": "Tomb Raider", "price_usd": "3500"},
    {"id": 3, "title": "Stray", "price_usd": "1000"},
]

inventory = {
    1: 10,
    2: 13,
    3: 4,
}

SHOP_FLAG_NAME = "test"


@app.route("/games", methods=["GET"])
def list_games():
    flags = flagsmith.get_environment_flags()

    try:
        metadata = json.loads(flags.get_feature_value(SHOP_FLAG_NAME))
        return jsonify(
            sorted(
                games,
                key=lambda i: i[metadata["default_sort_field"]],
                reverse=metadata["default_sort_direction"] == "desc",
            )
        )
    except (TypeError, KeyError) as e:
        pass

    return jsonify(games)

@app.route("/games/<int:game_id>/buy", methods=["POST"])
def buy_game(game_id: int):
    flags = flagsmith.get_environment_flags()
    if not flags.is_feature_enabled(SHOP_FLAG_NAME):
        return jsonify({"result": "error", "message": "Shop not yet available!"})

    if game_id not in inventory or inventory[game_id] == 0:
        return jsonify({"result": "error", "message": "Game not in stock!"})

    inventory[game_id] -= 1

    return {"result": "success", "message": "Game bought successfully."}
