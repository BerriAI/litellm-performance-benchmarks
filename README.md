# litellm-performance-benchmarks
A reproducible benchmarking suite for measuring LiteLLM latency, throughput, and scalability under real-world workloads.

## Running the load tests

The Locust files read the gateway key from the `API_KEY` environment variable and fail on startup when it is unset. Set it to the master key or virtual key of the gateway you are testing, then point Locust at that gateway

```bash
export API_KEY="<your gateway key>"
locust -f "litellm vs portkey vs kong (02_16_2026)/LiteLLM/LiteLLM_Locus_Load_Generator_File.py" --host http://localhost:4000/
```

The Portkey config and Locust file send `fake-api-key-for-example-endpoint` to the example OpenAI endpoint, which accepts any key. Replace it if you point Portkey at a real provider
