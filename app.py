from flask import Flask, request, send_file
from TTS.api import TTS

# Carrega o modelo (pode demorar no primeiro uso)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

app = Flask(__name__)

@app.route('/speak')
def speak():
    text = request.args.get('text', 'Hello world!')
    tts.tts_to_file(text=text, file_path="output.wav")
    return send_file("output.wav", mimetype="audio/wav")

app.run(host='0.0.0.0', port=5000)
