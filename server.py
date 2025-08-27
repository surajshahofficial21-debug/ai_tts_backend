from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from TTS.api import TTS
import os
import uuid

app = Flask(__name__)
CORS(app)

# Load Coqui TTS model once at startup
tts_model = TTS("tts_models/en/ljspeech/tacotron2-DDC")

@app.route("/tts", methods=["POST"])
def tts():
    try:
        data = request.json
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "No text provided"}), 400

        filename = f"{uuid.uuid4()}.wav"  # output as WAV
        tts_model.tts_to_file(text=text, file_path=filename)

        return send_file(filename, mimetype="audio/wav")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
