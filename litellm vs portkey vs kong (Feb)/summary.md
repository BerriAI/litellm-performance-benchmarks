# Latency Comparison Report

## 1. Render reported metrics


| Metric                 | **Kong**                           | **LiteLLM**                            | **Portkey**                          |
| :--------------------- | :--------------------------------- | :------------------------------------- | :----------------------------------- |
| **p50**                | ~27 ms                             | ~48 ms                                 | ~39 ms                               |
| **p75**                | ~30 ms                             | ~59 ms                                 | ~51 ms                               |
| **p90**                | ~38 ms                             | ~68 ms                                 | ~222 ms                              |
| **p99**                | ~56 ms                             | ~183 ms                                | ~805 ms                              |

---

## 2. Locust reported metrics

| Metric                 | **Kong**              | **LiteLLM**               | **Portkey**             |
| :--------------------- | :-------------------- | :------------------------ | :---------------------- |
| **p50**                | ~720 ms               | ~590 ms                   | ~780 ms                 |
| **p95**                | ~1,900 ms             | ~1,700 ms                 | ~2,100 ms               |
| **p99**                | ~2,800 ms             | ~2,500 ms                 | ~3,000 ms               |
| **Stability**          | 0% failures           | 0% failures               | 0% failures             |


# Test Specs

- Machine Specifications: 8 vCPUs, 32 GB RAM
- Test Duration: 1 hour
- Mock Endpoint: Deployed on Railway
- Gateways: LiteLLM, Portkey, and Kong deployed on Render