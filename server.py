from flask import Flask, request, send_file, jsonify
import subprocess
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)
PIPER_PATH = os.path.join(BASE_DIR, "bin", "piper")
MODEL_PATH = os.path.join(BASE_DIR, "model.onnx")
OUTPUT_FILE = os.path.join(BASE_DIR, "output.wav")

@app.route("/tts", methods=["POST"])
def tts():
    try:
        data = request.get_json()
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Run Piper from ./bin/piper
        subprocess.run([
            PIPER_PATH,
            "--model", MODEL_PATH,
            "--output", OUTPUT_FILE
        ], input=text.encode("utf-8"), check=True)

        return send_file(OUTPUT_FILE, mimetype="audio/wav")

    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Piper failed: {e}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
