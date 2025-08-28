from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import uuid
import os
import piper

app = Flask(__name__)
CORS(app)

# Piper model ek baar hi load karo
model = piper.load_model("en_US-amy-medium")  # Lightweight model

@app.route("/tts", methods=["POST"])
def tts():
    try:
        data = request.json
        text = data.get("text", "")
        if not text.strip():
            return jsonify({"error": "No text provided"}), 400

        filename = f"{uuid.uuid4()}.wav"
        with open(filename, "wb") as f:
            model.synthesize(text, f)  # WAV output

        return send_file(filename, mimetype="audio/wav", as_attachment=True, download_name="speech.wav")

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Optional: synthesized file remove karna chahe to
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
