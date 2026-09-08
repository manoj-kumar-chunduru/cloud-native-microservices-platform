# Cloud-Native Microservices Platform

A production-oriented microservices platform demonstrating scalable backend
architecture, REST APIs, distributed communication, caching, observability,
containerization, and cloud-native deployment.

## Overview

This project demonstrates how to design and deploy scalable microservices
using modern backend and cloud-native engineering practices.

The platform is designed around independently deployable services with clear
ownership boundaries, health checks, structured observability, automated
testing, containerization, and Kubernetes-ready deployment.

## Architecture

                    ┌─────────────────┐
                    │   API Gateway   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────▼─────┐  ┌────▼─────┐  ┌────▼─────┐
        │ User      │  │ Metadata │  │ Asset    │
        │ Service   │  │ Service  │  │ Service  │
        └─────┬─────┘  └────┬─────┘  └────┬─────┘
              │             │              │
              └─────────────┼──────────────┘
                            │
                     ┌──────▼──────┐
                     │ PostgreSQL  │
                     └──────┬──────┘
                            │
                     ┌──────▼──────┐
                     │    Redis    │
                     └─────────────┘

## Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL
- Redis
- Docker
- Kubernetes
- REST APIs
- GitHub Actions
- Prometheus
- Grafana
- Pytest

## Key Features

- Microservices-oriented architecture
- RESTful API design
- Database persistence boundary
- Redis caching boundary
- Health and readiness endpoints
- Structured application metrics
- Containerized deployment
- Kubernetes deployment manifests
- Horizontal scaling
- CI/CD pipeline
- Automated testing
- Security-conscious container configuration

## API Examples

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

## Project Structure

app/
├── main.py
│
tests/
└── test_api.py

k8s/
└── deployment.yaml

docs/
├── architecture.md
└── adr-001-production-boundaries.md

.github/
└── workflows/
    └── ci.yml

Dockerfile
docker-compose.yml
pyproject.toml
Makefile
README.md

## Running Locally

Clone the repository:

git clone <repository-url>

Install dependencies:

pip install -e '.[dev]'

Run the service:

make run

Or start it using Docker:

docker compose up --build

## Testing

Run the complete test suite:

pytest

The project includes:

- Unit tests
- API tests
- Validation scenarios
- Negative test scenarios
- Health-check validation
- HTTP contract validation

## Observability

The service exposes Prometheus-compatible metrics including:

- HTTP request rate
- HTTP error rate
- Request duration
- Service health
- Readiness state

Grafana can be connected to Prometheus for dashboards in a production
deployment.

## CI/CD

GitHub Actions automates:

1. Dependency installation
2. Static analysis
3. Type checking
4. Unit/API tests
5. Build validation

## Reliability Engineering

The architecture is designed around:

- Explicit service boundaries
- Health and readiness separation
- Idempotent operations where applicable
- Timeouts at network boundaries
- Retry only for safe transient failures
- Graceful degradation
- Horizontal scaling
- Fault isolation

## Security

- Non-root container execution
- Environment-based configuration
- No secrets committed to source control
- Input validation
- Least-privilege deployment guidance
- Production TLS and secret-manager recommendations

## Engineering Principles

- Loose coupling
- High cohesion
- Fault isolation
- Horizontal scalability
- Observability
- Infrastructure as Code
- Automated testing
- Secure-by-default development

## Future Improvements

- Separate User, Metadata, and Asset services
- PostgreSQL persistence
- Redis distributed caching
- Kafka event streaming
- gRPC for internal communication
- OpenTelemetry distributed tracing
- AWS deployment
- Service mesh
- Kubernetes autoscaling

## Author

Manoj Kumar Chunduru
Software Engineer
