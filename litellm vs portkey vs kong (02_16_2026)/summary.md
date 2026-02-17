# Why the Numbers Are Different (Render vs Locust)

* **Render metrics** measure time spent **inside Render** (gateway + upstream call).
  It **does not include the user’s internet connection latency**.

* **Locust metrics** measure what a user actually experiences — including how long it takes for the request to travel over the internet to Render and back.

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


# Gateway reference files

## Kong

* Config: [Kong_Config_File.yaml](Kong/Kong_Config_File.yaml)
* Locust load generator: [Kong_Locust_Load_Generator_File.py](Kong/Kong_Locust_Load_Generator_File.py)
* Locust Latency Chart: [Kong_Locust_Chart.png](Kong/Kong_Locust_Chart.png)
* Locust Latency Numbers: [Kong_Locust_Numbers.png](Kong/Kong_Locust_Numbers.png)
* Render Latency Numbers: [Kong_Render_Reported_Latency.png](Kong/Kong_Render_Reported_Latency.png)

## LiteLLM

* Config: [LiteLLM_Config_File.yaml](LiteLLM/LiteLLM_Config_File.yaml)
* Locust load generator: [LiteLLM_Locus_Load_Generator_File.py](LiteLLM/LiteLLM_Locus_Load_Generator_File.py)
* Locust Latency Chart: [LiteLLM_Locust_Chart.png](LiteLLM/LiteLLM_Locust_Chart.png)
* Locust Latency Numbers: [LiteLLM_Locust_Numbers.png](LiteLLM/LiteLLM_Locust_Numbers.png)
* Render Latency Numbers: [LiteLLM_Render_Reported_Latency.png](LiteLLM/LiteLLM_Render_Reported_Latency.png)

## Portkey

* Config: [Portkey_Config_File.json](Portkey/Portkey_Config_File.json)
* Locust load generator: [Portkey_Locust_Load_Generator_File.py](Portkey/Portkey_Locust_Load_Generator_File.py)
* Locust Latency Chart: [Portkey_Locust_Chart.png](Portkey/Portkey_Locust_Chart.png)
* Locust Latency Numbers: [Portkey_Locust_Numbers.png](Portkey/Portkey_Locust_Numbers.png)
* Render Latency Numbers: [Portkey_Render_Reported_Latency.png](Portkey/Portkey_Render_Reported_Latency.png)

---

# Test Specs

* **Machine Specifications:** 8 vCPUs, 32 GB RAM
* **Test Duration:** 1 hour
* **Mock Endpoint:** Deployed on Railway
* **Gateways:** LiteLLM, Portkey, and Kong deployed on Render

All gateways were tested under the same infrastructure conditions for fairness.
