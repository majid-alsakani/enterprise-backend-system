# Performance evidence

Measured 2026-11-16 in a development sandbox with Python 3.13.15, FastAPI TestClient: 20 warmups, 200 sequential GET / requests. Median 2.479 ms, p95 4.150 ms, p99 5.334 ms. Five contract tests passed.

These are IN-PROCESS measurements, excluding network, TLS, persistence and concurrent clients. No production throughput, availability or scalability claim has been verified. Dependency warning: installed Starlette TestClient recommends httpx2 for a future compatibility change.

Reproduce with `PYTHONPATH=. python tools/benchmark.py` after installing pytest/httpx. For deployment benchmarks publish the commit, CPU/RAM, dependencies, workers, dataset, concurrency, duration, error rate and repeated latency percentiles. Never present this local sample as production capacity.
