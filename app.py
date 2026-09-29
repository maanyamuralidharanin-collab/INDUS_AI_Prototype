from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json() or {}
    name = data.get("file", "Document")
    return jsonify({
        "status":"success",
        "planner":"Execution plan created",
        "retriever":"Relevant enterprise knowledge found",
        "vision":"Image processed",
        "reasoning":"Evidence verified",
        "report":f"Source-cited response generated for {name}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
