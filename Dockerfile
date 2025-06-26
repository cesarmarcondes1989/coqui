FROM python:3.10-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Expõe a porta do Flask
EXPOSE 5000

# Comando para iniciar o app
CMD ["python", "app.py"]
