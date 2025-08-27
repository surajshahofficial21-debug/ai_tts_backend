from flask import Flask, request, send_file
from gtts import gTTS
import tempfile

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return "No text provided", 400

    tts = gTTS(text)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)

    return send_file(temp_file.name, mimetype="audio/mpeg")

@app.route('/')
def home():
    return "TTS Backend Running!"
