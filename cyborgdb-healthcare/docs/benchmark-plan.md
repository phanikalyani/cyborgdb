# Benchmark Plan

1. Datasets: 10k, 100k, 1M passages (synthetic clinical notes).
2. Metrics: p50/p95/p99 latency, QPS, upsert throughput, CPU/RAM utilization.
3. Scenarios: single-tenant, 100 tenants, mixed workloads.
4. Tools: benchmark.py (included), Locust for load testing.
