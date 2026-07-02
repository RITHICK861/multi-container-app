from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import socket

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "TechNova Backend is Running!"


@app.route("/api")
def api():
    return jsonify({
        "company": "TechNova Solutions",
        "project": "Automated Multi-Container Deployment",
        "status": "Running Successfully",
        "version": "1.0.0",
        "server_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "hostname": socket.gethostname(),
        "technology": [
            "Flask",
            "Docker",
            "Docker Compose",
            "Jenkins",
            "GitHub"
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)