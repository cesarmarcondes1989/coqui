from flask import Flask, request, send_file, jsonify
from TTS.api import TTS
import os

app = Flask(__name__)

# Carrega modelo multilíngue do Coqui TTS
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_model", progress_bar=False, gpu=False)

@app.route("/speak", methods=["GET"])
def speak():
    try:
        text = request.args.get("text")
        speaker = request.args.get("speaker", None)
        language = request.args.get("language", "en")  # idioma padrão: inglês

        if not text:
            return jsonify({"error": "Missing 'text' parameter"}), 400

        output_path = "output.wav"

        tts.tts_to_file(
            text=text,
            speaker=speaker,
            language=language,
            file_path=output_path
        )

        return send_file(output_path, mimetype="audio/wav")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
