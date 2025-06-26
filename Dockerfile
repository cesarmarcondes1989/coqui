FROM python:3.10-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    libsndfile1 \
    espeak-ng \
    espeak-ng-data \
    && rm -rf /var/lib/apt/lists/*


# Define diretório de trabalho
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
