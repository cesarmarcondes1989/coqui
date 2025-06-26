FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    git \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN python -c "from TTS.api import TTS; TTS(model_name='tts_models/en/vctk/vits', progress_bar=False, gpu=False)"

EXPOSE 5000

CMD ["python", "app.py"]
