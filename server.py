import subprocess
import uuid
from flask import Flask, request, send_file, jsonify

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    text = request.json.get("text", "")
    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    # Output file का unique नाम
    filename = f"{uuid.uuid4()}.wav"

    # Piper को CLI mode में call करना
    result = subprocess.run([
        "piper",
        "--model", "en_US-amy-medium",
        "--output_file", filename
    ], input=text.encode("utf-8"), capture_output=True)

    if result.returncode != 0:
        return jsonify({"error": result.stderr.decode("utf-8")}), 500

    return send_file(filename, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
