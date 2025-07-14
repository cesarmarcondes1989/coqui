from flask import Flask, request, send_file, jsonify
from TTS.api import TTS
import os

app = Flask(__name__)

# Carrega modelo multi-speaker
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=False)

@app.route("/speak", methods=["GET"])
def speak():
    try:
        text = request.args.get("text")
        if not text:
            return jsonify({"error": "Missing 'text' parameter"}), 400

        # Pega o speaker da URL ou usa o primeiro como padrão
        speaker = request.args.get("speaker", default=tts.speakers[0])

        output_path = "output.wav"
        tts.tts_to_file(text=text, speaker=speaker, file_path=output_path)

        return send_file(output_path, mimetype="audio/wav")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/speakers", methods=["GET"])
def get_speakers():
    return jsonify({"speakers": tts.speakers})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
