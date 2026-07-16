@app.route("/generate-post", methods=["POST"])
def generate_post():
    try:
        data = request.get_json(force=True)
        return jsonify({
            "success": True,
            "received": data
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
