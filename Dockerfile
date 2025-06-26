# Usa imagem base leve com Python
FROM python:3.10-slim

# Define variáveis de ambiente para evitar prompts e avisos
ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8

# Atualiza e instala dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    espeak-ng \
    libespeak-ng1 \
    ffmpeg \
    curl \
    build-essential \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Cria e define o diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação
COPY . /app

# Instala dependências do projeto
RUN pip install --upgrade pip
RUN pip install TTS

# Baixa o modelo pré-treinado (opcional: pode ser feito via script Python também)
# RUN TTS --list_models  # Use este comando para ver os modelos disponíveis
# RUN TTS --model_name "tts_models/en/vctk/vits" --text "Hello world"

# Porta padrão (caso use API)
EXPOSE 5000

# Comando padrão para iniciar o app
CMD ["python", "app.py"]
