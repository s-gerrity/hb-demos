from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/name-to-code.json")
def name_to_code():
    """Convert a state name to a 2-letter code.

    (For the sake of having an API for this, we're implementing it ourselves.
    In our example, though, this will be coming from some external API.
    """
    state_codes = {"California": "CA",
                   "Texas": "TX",
                   "Oregon": "OR",
                   }
    state = request.values.get("state")
    code = state_codes.get(state)
    return jsonify({"code": code})


if __name__ == "__main__":
    app.run(port=5001)
