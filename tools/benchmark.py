import json
import platform
import statistics
import time
from fastapi.testclient import TestClient
from app.main import app


def main():
    durations = []
    with TestClient(app) as client:
        for _ in range(20):
            assert client.get('/').status_code == 200
        for _ in range(200):
            start = time.perf_counter()
            response = client.get('/')
            durations.append((time.perf_counter() - start) * 1000)
            if response.status_code != 200:
                raise RuntimeError(f'Unexpected HTTP {response.status_code}')
    ordered = sorted(durations)
    print(json.dumps({'python': platform.python_version(), 'requests': 200,
                      'mode': 'sequential in-process TestClient, no network',
                      'median_ms': round(statistics.median(ordered), 3),
                      'p95_ms': round(ordered[189], 3),
                      'p99_ms': round(ordered[197], 3)}, indent=2))


if __name__ == '__main__':
    main()
