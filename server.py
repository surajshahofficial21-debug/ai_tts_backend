from flask import Flask, request, send_file
import subprocess
import tempfile
import os

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}, 400

    # Temporary output file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp_name = tmp.name

    # Piper command
    cmd = [
        "piper",
        "--model", "voices/en_US-libritts-high.onnx",
        "--output_file", tmp_name
    ]

    try:
        # Run Piper as subprocess
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        process.communicate(input=text.encode("utf-8"))

        if process.returncode != 0:
            return {"error": "Piper failed to generate audio"}, 500

        # Send back generated WAV file
        return send_file(tmp_name, mimetype="audio/wav")

    finally:
        if os.path.exists(tmp_name):
            os.remove(tmp_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
