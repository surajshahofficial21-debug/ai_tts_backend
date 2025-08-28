from flask import Flask, request, send_file
import subprocess
import io
import wave

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data.get("text", "")

    # Run Piper to get raw audio (16-bit PCM)
    cmd = ["piper", "--model", "voices/en_US-libritts-high.onnx", "--output_raw"]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    raw_audio, _ = process.communicate(input=text.encode("utf-8"))

    # Convert raw PCM to proper WAV
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, "wb") as wf:
        wf.setnchannels(1)         # mono
        wf.setsampwidth(2)         # 16-bit
        wf.setframerate(22050)     # sample rate
        wf.writeframes(raw_audio)

    wav_buffer.seek(0)
    return send_file(wav_buffer, mimetype="audio/wav", as_attachment=True, download_name="output.wav")

@app.route('/')
def home():
    return "TTS server running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
