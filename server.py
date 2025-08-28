from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import subprocess
import uuid

app = Flask(__name__)
CORS(app)

# Root route for Render health check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "TTS API is running"}), 200

# Text-to-Speech route
@app.route("/tts", methods=["POST"])
def tts():
    try:
        data = request.json
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "No text provided"}), 400

        # Temporary audio file
        filename = f"{uuid.uuid4()}.wav"
        
        # Run Piper TTS via subprocess
        subprocess.run(
            ["piper", "--model", "en_US-amy-medium", "--output_file", filename],
            input=text.encode("utf-8"),
            check=True
        )

        return send_file(filename, mimetype="audio/wav")

    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Piper failed: {e}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
