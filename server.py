from flask import Flask, request, send_file, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "ok", "message": "TTS server running"}), 200

@app.route('/tts', methods=['POST'])
def tts():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data['text']
        output_file = "output.wav"

        subprocess.run(
            ["./piper/piper", "--model", "voices/en_US-amy-low.onnx", "--output_file", output_file],
            input=text.encode("utf-8"),
            check=True
        )

        return send_file(output_file, mimetype="audio/wav")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
