# Latency Comparison Report

## 1. Render reported metrics


| Metric                 | **Kong**                           | **LiteLLM**                            | **Portkey**                          |
| :--------------------- | :--------------------------------- | :------------------------------------- | :----------------------------------- |
| **p50**                | ~27 ms                             | ~48 ms                                 | ~39 ms                               |
| **p75**                | ~30 ms                             | ~59 ms                                 | ~51 ms                               |
| **p90**                | ~38 ms                             | ~68 ms                                 | ~222 ms                              |
| **p99**                | ~56 ms                             | ~183 ms                                | ~805 ms                              |
| **Stability**          | Very stable                        | Mostly stable (minor spike)            | High tail volatility                 |
| **Overall Assessment** | Lowest latency and most consistent | Moderate latency, slight tail increase | Significant tail latency degradation |

---

## 2. Locust reported metrics

| Metric                 | **Kong**              | **LiteLLM**               | **Portkey**             |
| :--------------------- | :-------------------- | :------------------------ | :---------------------- |
| **p50**                | ~720 ms               | ~590 ms                   | ~780 ms                 |
| **p95**                | ~1,900 ms             | ~1,700 ms                 | ~2,100 ms               |
| **p99**                | ~2,800 ms             | ~2,500 ms                 | ~3,000 ms               |
| **Stability**          | 0% failures           | 0% failures               | 0% failures             |
| **Overall Assessment** | Strong and consistent | Lowest latency under load | Highest overall latency |

### Summary

* Under concurrency, LiteLLM achieves the lowest median and tail latency.
* Kong remains stable and competitive.
* Portkey shows the highest overall latency, though reliability remained stable with no failures observed.
