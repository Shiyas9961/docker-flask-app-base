from flask import Flask, jsonify
import os

app = Flask(__name__)
PORT = os.environ.get("PORT")

@app.route("/")
def run():
    return jsonify({"message": "Hello, World!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)