<<<<<<< HEAD
# 📝 HandDoc AI – OCR Inteligente para Documentos Manuscritos

[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

> Reconhecimento de escrita à mão com IA para uso em apps móveis e automação de leitura de documentos.

---

## 📌 Visão Geral

O **HandDoc AI** é uma plataforma completa de OCR que utiliza **Inteligência Artificial** para ler textos manuscritos com alta precisão. Projetado para integrar com aplicativos móveis Android, ele extrai conteúdo de documentos com complexidade visual, como formulários preenchidos à mão.

🚀 Combinamos IA avançada com uma API moderna, leve e escalável.

---

## 🔧 Tecnologias Utilizadas

| Camada        | Ferramenta/Framework                    |
|---------------|-----------------------------------------|
| 📱 Frontend   | Java (Android Studio)                   |
| 🧠 Backend    | Python 3.11, FastAPI                     |
| 🔍 IA OCR     | Transformers (TrOCR da Microsoft)       |
| 🎯 Alternativa| EasyOCR (fallback)                      |
| 🖼️ Processamento | OpenCV, Pillow (PIL)                  |
| 🗄️ Banco de Dados | PostgreSQL (via Docker)             |
| 🐳 Infraestrutura | Docker, Docker Compose, GitHub     |

---

## ✅ Funcionalidades

- 🔠 OCR com IA (TrOCR e fallback para EasyOCR)
- 🚀 API REST com FastAPI
- 🗃️ Armazenamento automático de resultados no PostgreSQL
- 📸 Integração com app Android para captura de imagens
- 📂 Upload e leitura de imagens locais
- ⚙️ Arquitetura pronta para escalar com containers

---

## 🗂️ Estrutura de Pastas

handdoc-ai/
├── app/
│ ├── main.py # Entrypoint FastAPI
│ ├── ocr.py # Módulo principal de OCR (TrOCR / EasyOCR)
│ ├── database.py # Conexão com PostgreSQL via SQLAlchemy
│ ├── models.py # ORM (Modelos de Tabelas)
│ ├── schemas.py # Validação com Pydantic (opcional)
│ └── utils.py # Funções auxiliares
│
├── static/
│ └── uploads/ # Imagens enviadas
│
├── tests/
│ └── test_ocr.py # Testes automatizados (opcional)
│
├── Dockerfile # Container do backend
├── docker-compose.yml # Orquestração dos containers
├── requirements.txt # Dependências Python
├── .env # Variáveis de ambiente
└── README.md # Documentação do projeto




## 📷 Integração com Android

O app Android envia uma imagem via POST para a rota:

POST /ocr/
Content-Type: multipart/form-data
A resposta será:

    json
    {
    "id": 1,
    "filename": "exemplo.png",
    "text": "Texto reconhecido...",
    "created_at": "2025-06-13T19:00:00"
    }


## 🤖 Créditos

🤗 Transformers – Hugging Face

EasyOCR

FastAPI

PostgreSQL


=======
# 📝 HandDoc AI – OCR Inteligente para Documentos Manuscritos

[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

> Reconhecimento de escrita à mão com IA para uso em apps móveis e automação de leitura de documentos.

---

## 📌 Visão Geral

O **HandDoc AI** é uma plataforma completa de OCR que utiliza **Inteligência Artificial** para ler textos manuscritos com alta precisão. Projetado para integrar com aplicativos móveis Android, ele extrai conteúdo de documentos com complexidade visual, como formulários preenchidos à mão.

🚀 Combinamos IA avançada com uma API moderna, leve e escalável.

---

## 🔧 Tecnologias Utilizadas

| Camada        | Ferramenta/Framework                    |
|---------------|-----------------------------------------|
| 📱 Frontend   | Java (Android Studio)                   |
| 🧠 Backend    | Python 3.11, FastAPI                     |
| 🔍 IA OCR     | Transformers (TrOCR da Microsoft)       |
| 🎯 Alternativa| EasyOCR (fallback)                      |
| 🖼️ Processamento | OpenCV, Pillow (PIL)                  |
| 🗄️ Banco de Dados | PostgreSQL (via Docker)             |
| 🐳 Infraestrutura | Docker, Docker Compose, GitHub     |

---

## ✅ Funcionalidades

- 🔠 OCR com IA (TrOCR e fallback para EasyOCR)
- 🚀 API REST com FastAPI
- 🗃️ Armazenamento automático de resultados no PostgreSQL
- 📸 Integração com app Android para captura de imagens
- 📂 Upload e leitura de imagens locais
- ⚙️ Arquitetura pronta para escalar com containers

---

## 🗂️ Estrutura de Pastas

handdoc-ai/
├── app/
│ ├── main.py # Entrypoint FastAPI
│ ├── ocr.py # Módulo principal de OCR (TrOCR / EasyOCR)
│ ├── database.py # Conexão com PostgreSQL via SQLAlchemy
│ ├── models.py # ORM (Modelos de Tabelas)
│ ├── schemas.py # Validação com Pydantic (opcional)
│ └── utils.py # Funções auxiliares
│
├── static/
│ └── uploads/ # Imagens enviadas
│
├── tests/
│ └── test_ocr.py # Testes automatizados (opcional)
│
├── Dockerfile # Container do backend
├── docker-compose.yml # Orquestração dos containers
├── requirements.txt # Dependências Python
├── .env # Variáveis de ambiente
└── README.md # Documentação do projeto




## 📷 Integração com Android

O app Android envia uma imagem via POST para a rota:

POST /ocr/
Content-Type: multipart/form-data
A resposta será:

    json
    {
    "id": 1,
    "filename": "exemplo.png",
    "text": "Texto reconhecido...",
    "created_at": "2025-06-13T19:00:00"
    }


## 🤖 Créditos

🤗 Transformers – Hugging Face

EasyOCR

FastAPI

PostgreSQL


>>>>>>> 15efedc67d922f65eca78f7d07c34d943f10aeba
