# Compliance Notes (Healthcare / HIPAA)

- Keep CyborgDB proxy inside customer VPC or on-prem.
- Use customer-managed KMS keys; do not store keys in vendor-controlled storage.
- Maintain immutable audit logs with redaction: log query hash, tenant, actor id, timestamp.
- Provide Business Associate Agreement (BAA) if using third-party LLM provider.
