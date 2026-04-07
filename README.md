# devops.ci.api 🚀

API de exemplo construída com **FastAPI** para demonstrar pipeline CI/CD 
com GitHub Actions e deploy no AWS AppRunner.

## Estrutura


devops.ci.api/
├── app/
│   ├── main.py           # Aplicação FastAPI
│   └── requirements.txt  # Dependências
├── tests/
│   └── test_main.py      # Testes automatizados
├── Dockerfile            # Build da imagem
└── .github/
└── workflows/
└── ci-cd.yml     # Pipeline CI/CD


## Endpoints

| Método | Endpoint  | Descrição |
|--------|-----------|-----------|
| GET | `/`       | Informações da API |
| GET | `/health` | Health check |
| GET | `/info`   | Informações do ambiente |

## Como rodar localmente
```bash
# Instalar dependências
pip install -r app/requirements.txt

# Rodar a aplicação
uvicorn app.main:app --reload --port 8000

# Rodar os testes
pytest tests/
```

## Como rodar com Docker
```bash
# Build
docker build -t davops-api .

# Run
docker run -p 8000:8000 -e ENV=local davops-api
```

## Pipeline CI/CD

| Estágio | Descrição |
|---------|-----------|
| Test | Roda os testes automatizados |
| Build | Constrói a imagem Docker |
| Push ECR | Envia a imagem para o ECR |
| Deploy Dev | Deploy no AppRunner dev |
| Health Check | Verifica saúde da aplicação em dev |
| Deploy Prod | Deploy no AppRunner prod |