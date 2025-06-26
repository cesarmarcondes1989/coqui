FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    git ffmpeg espeak-ng libsndfile1-dev curl \
    && pip install --upgrade pip \
    && pip install flask TTS

WORKDIR /app
COPY . /app

CMD ["python", "app.py"]
