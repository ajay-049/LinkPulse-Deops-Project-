# LinkPulse — Cloud-Native URL Shortener & Analytics Platform

A microservices-based URL shortener built to demonstrate production Kubernetes, Docker, CI/CD, security, and observability patterns.

## Architecture
- **API Service:** Python FastAPI (URL creation & redirects)
- **Worker Service:** Python background worker (click analytics)
- **Cache/Queue:** Redis
- **Database:** MySQL (StatefulSet + PersistentVolume)
- **Frontend:** Nginx reverse proxy + UI

## Progress Log
- [x] Phase 1: Containerize API Service (Non-root slim Docker image)
- [ ] Phase 2: Core K8s Deployment, ConfigMaps, Secrets & Services
- [ ] Phase 3: Stateful MySQL & Persistent Storage
- [ ] Phase 4: Ingress Routing & TLS
- [ ] Phase 5: Health Probes, Resource Limits & HPA Autoscaling
- [ ] Phase 6: Zero-Trust Security (RBAC & NetworkPolicies)
- [ ] Phase 7: Helm Charts & GitHub Actions CI/CD
- [ ] Phase 8: Prometheus & Grafana Observability
