from flask import Flask, request, send_file, jsonify
import subprocess
import traceback
import os

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    try:
        data = request.get_json(force=True)
        text = data.get("text", "").strip()
        print(f"[DEBUG] Received text: {text}", flush=True)

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Output wav file
        output_path = "output.wav"

        # Call Piper TTS (change path/model if needed)
        cmd = [
            "piper", 
            "--model", "en_US-amy-medium", 
            "--output_file", output_path
        ]
        print(f"[DEBUG] Running command: {' '.join(cmd)}", flush=True)
        
        # Run Piper with input text
        process = subprocess.run(cmd, input=text.encode(), capture_output=True)
        
        if process.returncode != 0:
            print("[ERROR] Piper failed", flush=True)
            print(process.stderr.decode(), flush=True)
            return jsonify({"error": "Piper TTS failed"}), 500

        print("[DEBUG] Piper completed successfully", flush=True)

        # Send wav back to client
        return send_file(output_path, mimetype="audio/wav")

    except Exception as e:
        print("[ERROR] Exception in /tts:", e, flush=True)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
