# FastAPI CI/CD Demo API

Containerized FastAPI application used to demonstrate a DevOps pipeline with automated tests, Docker image build, Amazon ECR publishing and AWS App Runner deployment.

This repository is part of a pair:

- Application repository: `DavidDevd/devops.ci.api`
- Infrastructure repository: `DavidDevd/devops.ci.iac`

## What This Project Shows

- FastAPI application with simple health endpoints
- Automated tests with `pytest`
- Docker image build
- CI/CD workflow with GitHub Actions
- Deployment target designed for AWS App Runner

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | API metadata |
| GET | `/health` | Health check endpoint |
| GET | `/info` | Runtime environment information |

## Run Locally

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Run Tests

```bash
pytest tests/
```

## Run With Docker

```bash
docker build -t davops-api .
docker run -p 8000:8000 -e ENV=local davops-api
```

## CI/CD Flow

```text
Push to GitHub
  -> Run tests
  -> Build Docker image
  -> Push image to Amazon ECR
  -> Deploy to AWS App Runner
  -> Validate health endpoint
```

## Related Project

Infrastructure for this API is available at:

https://github.com/DavidDevd/devops.ci.iac

