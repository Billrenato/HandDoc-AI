# Imagem base com Python 3.11
FROM python:3.13-slim

# Evita prompt do apt
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências do sistema para OCR e libs Python
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /app

# Copia o requirements.txt e instala as dependências
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o restante da aplicação
COPY . .

# Cria diretório de uploads (caso não exista)
RUN mkdir -p static/uploads

# Expõe a porta da aplicação
EXPOSE 8000

# Comando padrão (caso queira rodar standalone sem docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]