from flask import Flask, request, send_file
from TTS.api import TTS
import time

MODEL = "tts_models/multilingual/multi-dataset/your_tts"
tts = TTS(model_name=MODEL, progress_bar=False)

app = Flask(__name__)

@app.route('/speak')
def speak():
    text = request.args.get('text', 'Hello world!')
    speaker = request.args.get('speaker', tts.speakers[0])  # usa o primeiro speaker como padrão
    start = time.time()
    print(f"🔊 Texto: {text} | Voz: {speaker}")
    tts.tts_to_file(text=text, speaker=speaker, file_path="output.wav")
    print(f"✅ Áudio gerado em {time.time() - start:.2f}s")
    return send_file("output.wav", mimetype="audio/wav")

@app.route('/speakers')
def list_speakers():
    return {"available_speakers": tts.speakers}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
