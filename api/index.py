from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/api/post_question", methods=["GET"])
def test():
    text = ""
    with open('ll.txt', 'r') as f:
        text = f.readline()
    return jsonify({"status": "success", "message": text})

if __name__ == "__main__":
    app.run()
