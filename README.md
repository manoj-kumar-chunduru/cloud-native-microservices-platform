# Cloud-Native Microservices Platform

A cloud-native backend reference implementation demonstrating REST API
design, request validation, health and readiness checks, observability,
automated testing, containerization, and Kubernetes deployment practices.

> This repository is intentionally presented as a reference implementation.
> The current version uses an in-memory persistence layer. PostgreSQL,
> Redis, independent service boundaries, and distributed communication are
> planned extensions rather than implemented production infrastructure.

## Overview

This project demonstrates engineering practices used when building
cloud-native backend services.

The current implementation focuses on:

- REST API design
- Request validation
- Health and readiness checks
- Prometheus-compatible metrics
- Automated API testing
- Static analysis and type checking
- Containerized execution
- Kubernetes deployment configuration
- CI quality gates
- Security-conscious container configuration

The implementation is intentionally small and self-contained so that the
engineering behavior can be inspected, tested, and extended easily.

## Current Architecture

The current implementation is a lightweight FastAPI reference service.

```text
Client
  |
  v
FastAPI Application
  |
  +---- User API
  |
  +---- Health / Readiness
  |
  +---- Prometheus Metrics
  |
  v
In-Memory User Store```

## Implemented Capabilities

### REST API

- `POST /api/v1/users`
- `GET /api/v1/users/{id}`
- Request validation
- Response validation
- HTTP 404 handling for missing resources
- HTTP 422 validation responses

### Reliability and Operations

- `/health` liveness endpoint
- `/ready` readiness endpoint
- `/metrics` observability endpoint
- HTTP request metrics
- Request duration metrics
- Container health checking
- Kubernetes liveness probe
- Kubernetes readiness probe

### Testing

The project includes automated tests covering:

- Health endpoint
- User creation
- User retrieval
- Input validation
- Missing-resource handling
- API behavior

### Code Quality

The CI pipeline validates:

1. Ruff static analysis
2. Mypy type checking
3. Pytest test suite

## Technology Stack

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Prometheus Client
- Pytest
- Ruff
- Mypy
- Docker
- Docker Compose
- Kubernetes
- GitHub Actions

## API

### Health Check

GET /health

### Readiness Check

GET /ready

### Create User

POST /api/v1/users

### Retrieve User

GET /api/v1/users/{id}

### Metrics

GET /metrics

Interactive API documentation is available through FastAPI/OpenAPI when the
application is running:

http://localhost:8000/docs

## Project Structure

app/
└── main.py

tests/
└── test_api.py

k8s/
└── deployment.yaml

docs/
├── architecture.md
└── adr-001-boundaries.md

.github/
└── workflows/
    └── ci.yml

Dockerfile
docker-compose.yml
pyproject.toml
Makefile
README.md

## Running Locally

### Create a virtual environment

python -m venv .venv

### Linux/macOS

source .venv/bin/activate

### Windows

.venv\Scripts\Activate.ps1

### Install development dependencies

pip install -e ".[dev]"

### Run the service

make run

Or:

uvicorn app.main:app --reload

The API will be available at:

http://localhost:8000

## Docker

Build and start the application:

docker compose up --build

The container is configured to run using a non-root user.

## Testing

Run the complete test suite:

pytest

Run static analysis:

ruff check .

Run type checking:

mypy app

The test suite focuses on API behavior, validation, health checks, and
negative scenarios.

## Observability

The service exposes Prometheus-compatible metrics through:

GET /metrics

The current implementation provides application-level HTTP metrics such as:

- Request count
- HTTP response status
- Request duration

Prometheus and Grafana can be integrated in a larger deployment environment.

No production monitoring or performance results are claimed by this
repository.

## Kubernetes

The repository includes Kubernetes deployment configuration demonstrating:

- Application deployment
- Multiple replicas
- Liveness probing
- Readiness probing
- Resource requests
- Resource limits
- Service exposure

The Kubernetes configuration is a deployment baseline and should not be
interpreted as evidence of a production cloud deployment.

The current application uses in-memory state. Therefore, running multiple
replicas does not provide shared persistent application state.

A production deployment would require an external durable persistence layer
and appropriate distributed-state management.

## CI/CD

GitHub Actions validates the project through automated quality checks.

The pipeline includes:

1. Dependency installation
2. Static analysis
3. Type checking
4. Automated tests
5. Build validation

## Reliability Engineering

The current implementation demonstrates:

- Health and readiness separation
- Input validation
- Negative-path testing
- Container health checking
- Kubernetes health probes
- Resource limits
- Graceful application lifecycle handling where implemented

Future distributed reliability capabilities will be added only when they are
implemented and tested.

## Security

Current security-oriented practices include:

- Non-root container execution
- Environment-based configuration
- No secrets committed to source control
- Input validation
- Resource limits
- Security documentation

Production TLS, external secret management, authentication, authorization,
and network policies are considered deployment-level extensions.

## Engineering Principles

- Correctness before scale
- Explicit boundaries
- Automated testing
- Observable services
- Secure container execution
- Reproducible development
- Infrastructure as Code
- Honest performance and deployment claims
- Incremental evolution of system architecture

## Planned Extensions

The following capabilities are planned extensions and are not currently
implemented production infrastructure:

- PostgreSQL persistence
- Redis distributed caching
- Independent User, Metadata, and Asset services
- API Gateway
- Kafka event streaming
- gRPC internal communication
- OpenTelemetry distributed tracing
- Kubernetes autoscaling
- AWS deployment
- Service mesh
- Distributed configuration
- Authentication and authorization

## Engineering Roadmap

The intended evolution of the platform is:

Current Reference Service
        |
        v
Persistence Abstraction
        |
        v
PostgreSQL Integration
        |
        v
Redis Caching
        |
        v
Independent Service Boundaries
        |
        v
Distributed Communication
        |
        v
Production-Oriented Cloud Deployment

Each stage will be implemented, tested, and documented before being
represented as an implemented capability.

## Author

Manoj Kumar Chunduru

Software Engineer
