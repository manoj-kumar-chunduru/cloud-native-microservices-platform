# ADR-001: Keep Infrastructure Behind Boundaries

## Decision
Business behavior is separated from cloud/vendor infrastructure through small interfaces or adapters. Local implementations keep development and tests fast; production deployments can substitute managed services.

## Rationale
This improves test isolation, migration flexibility and operational clarity without hiding important failure semantics.
