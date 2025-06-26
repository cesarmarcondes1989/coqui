from flask import Flask, request, send_file
from TTS.api import TTS
import time

# Modelo mais natural e expressivo com suporte a múltiplos idiomas
MODEL = "tts_models/multilingual/multi-dataset/your_tts"
tts = TTS(model_name=MODEL, progress_bar=False)

app = Flask(__name__)

@app.route('/speak')
def speak():
    text = request.args.get('text', 'Hello world!')
    start = time.time()
    print(f"🔊 Texto recebido: {text}")
    tts.tts_to_file(text=text, file_path="output.wav")
    print(f"✅ Áudio gerado em {time.time() - start:.2f}s")
    return send_file("output.wav", mimetype="audio/wav")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

