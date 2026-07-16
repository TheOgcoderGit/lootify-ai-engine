from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "Lootify AI v2",
        "status": "Running"
    })

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({
        "success": True,
        "message": "API Working"
    })

@app.route("/generate-post", methods=["POST"])
def generate_post():
    try:
        data = request.get_json(silent=True)

        if data is None:
            return jsonify({
                "success": False,
                "error": "Invalid JSON body"
            }), 400

        return jsonify({
            "success": True,
            "received": data
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "success": False,
        "error": "Route Not Found"
    }), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "success": False,
        "error": "Method Not Allowed"
    }), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
