# Latency Comparison Report

## Why the Numbers Are Different (And Why That Matters)

* **Render metrics** measure how long the request takes **inside Render** — from when the gateway receives the request to when it sends the response back.
  This includes gateway processing and the upstream provider call, but **does not include the user’s internet connection**.

* **Locust metrics** measure what a user would actually experience.
  This includes:

  * The user’s own internet connection
  * Internet routing and network variability
  * Gateway processing
  * Upstream provider response time
  * The return trip back to the user

* Locust numbers are higher because they measure the **full end-to-end journey**, including real-world internet conditions.

---

## 1. Render Reported Metrics

*(Server-side latency inside Render)*

| Metric  | **Kong** | **LiteLLM** | **Portkey** |
| :------ | :------- | :---------- | :---------- |
| **p50** | ~27 ms   | ~48 ms      | ~39 ms      |
| **p75** | ~30 ms   | ~59 ms      | ~51 ms      |
| **p90** | ~38 ms   | ~68 ms      | ~222 ms     |
| **p99** | ~56 ms   | ~183 ms     | ~805 ms     |

These numbers represent time spent inside Render (gateway + upstream call), not user-facing internet latency.

---

## 2. Locust Reported Metrics

*(Full user-observed latency)*

| Metric        | **Kong**    | **LiteLLM** | **Portkey** |
| :------------ | :---------- | :---------- | :---------- |
| **p50**       | ~720 ms     | ~590 ms     | ~780 ms     |
| **p95**       | ~1,900 ms   | ~1,700 ms   | ~2,100 ms   |
| **p99**       | ~2,800 ms   | ~2,500 ms   | ~3,000 ms   |
| **Stability** | 0% failures | 0% failures | 0% failures |

These numbers reflect what a real user experiences over the internet.

---

# Test Specs

* **Machine Specifications:** 8 vCPUs, 32 GB RAM
* **Test Duration:** 1 hour
* **Mock Endpoint:** Deployed on Railway
* **Gateways:** LiteLLM, Portkey, and Kong deployed on Render

All gateways were tested under the same infrastructure conditions for fairness.
