import os
import uuid
import json
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(0.5, 1)  # Random wait time between requests

    def on_start(self):
        self.api_key = "sk-1234"
        self.client.headers.update({'Authorization': f'Bearer {self.api_key}'})
        
        # Portkey config header (same as k6 script)
        portkey_config = {
            "strategy": {"mode": "fallback"},
            "targets": [
                {
                    "provider": "openai",
                    "api_key": self.api_key,
                    "custom_host": "https://exampleopenaiendpoint-production-0ee2.up.railway.app",
                    "request_timeout": 10000,
                    "weight": 1,
                }
            ],
            "cache": {"mode": "semantic", "max_age": 3600},
            "retry": {"attempts": 3, "on_status_codes": [408, 429, 500, 502, 503, 504]},
        }
        self.client.headers.update({'x-portkey-config': json.dumps(portkey_config)})

    @task
    def portkey_completion(self):
        # no cache hits with this
        payload = {
            "model": "db-openai-endpoint",
            "messages": [{"role": "user", "content": f"{uuid.uuid4()} This is a test there will be no cache hits and we'll fill up the context" * 150}],
            "user": "my-new-end-user-1"
        }
        response = self.client.post("v1/chat/completions", json=payload)
        
        if response.status_code != 200:
            # log the errors in error.txt
            with open("error.txt", "a") as error_log:
                error_log.write(response.text + "\n")
