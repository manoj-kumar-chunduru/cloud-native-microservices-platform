# Architecture

The local service uses an in-memory repository so it runs without infrastructure. Production adapters should use PostgreSQL and Redis.

## Reliability
Use bounded timeouts, retries only for transient/idempotent operations, rate limits, circuit breakers, graceful shutdown and dependency health signals.

## Observability
Use RED metrics (rate, errors, duration), structured logs and OpenTelemetry traces across service boundaries.

## Security
Use workload identity/IAM, secret managers, TLS, network policies and non-root containers.
