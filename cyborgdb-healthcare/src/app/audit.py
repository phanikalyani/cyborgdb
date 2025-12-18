import time, json, os
AUDIT_LOG = os.environ.get('AUDIT_LOG_PATH', '/data/audit.log')

def upload_audit_event(tenant_id, action, details):
    entry = {'ts': time.time(), 'tenant': tenant_id, 'action': action, 'details': details}
    # append-only
    with open(AUDIT_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
