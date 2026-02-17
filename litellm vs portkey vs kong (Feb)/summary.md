# Latency Comparison Report

## Why the Numbers Are Different

* **Render metrics** measure time spent **inside Render** (gateway + upstream call).
  They **do not include the user’s internet connection**.

* **Locust metrics** measure what a user actually experiences — including **the user’s own network connection over the internet**.

* The main difference is that Locust includes **real-world internet latency**, which is why those numbers are higher.


## 1. Render Reported Metrics

*(Server-side latency inside Render)*

| Metric  | **Kong** | **LiteLLM** | **Portkey** |
| :------ | :------- | :---------- | :---------- |
| **p50** | ~27 ms   | ~48 ms      | ~39 ms      |
| **p75** | ~30 ms   | ~59 ms      | ~51 ms      |
| **p90** | ~38 ms   | ~68 ms      | ~222 ms     |
| **p99** | ~56 ms   | ~183 ms     | ~805 ms     |

## 2. Locust Reported Metrics

*(Full user-observed latency)*

| Metric        | **Kong**    | **LiteLLM** | **Portkey** |
| :------------ | :---------- | :---------- | :---------- |
| **p50**       | ~720 ms     | ~590 ms     | ~780 ms     |
| **p95**       | ~1,900 ms   | ~1,700 ms   | ~2,100 ms   |
| **p99**       | ~2,800 ms   | ~2,500 ms   | ~3,000 ms   |


# Test Specs

* **Machine Specifications:** 8 vCPUs, 32 GB RAM
* **Test Duration:** 1 hour
* **Mock Endpoint:** Deployed on Railway
* **Gateways:** LiteLLM, Portkey, and Kong deployed on Render

All gateways were tested under the same infrastructure conditions for fairness.
