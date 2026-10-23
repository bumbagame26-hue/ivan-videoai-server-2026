
import os
import tempfile
import subprocess
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "app": "VideoAI Studio Ivan",
        "status": "online",
        "message": "Video translation backend is running"
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.post("/process")
def process_video():
    if "video" not in request.files:
        return jsonify({
            "error": "Upload a video using the field named 'video'."
        }), 400

    video = request.files["video"]
    if not video.filename:
        return jsonify({"error": "No video selected."}), 400

    return jsonify({
        "status": "received",
        "filename": video.filename,
        "message": (
            "Video upload endpoint is working. "
            "AI translation and dubbing are not connected yet."
        )
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
