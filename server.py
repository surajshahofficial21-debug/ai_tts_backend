from flask import Flask, request, send_file
import subprocess

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    data = request.json
    text = data.get("text", "")
    output_file = "output.wav"
    subprocess.run(["./piper", "--text", text, "--output_file", output_file], check=True)
    return send_file(output_file, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
