import requests
from config.config import COMMON_PATHS
from urllib.parse import urljoin

def check_common_paths(base_url):
    findings = []

    for path in COMMON_PATHS:
        full_url = urljoin(base_url, path)
        try:
            res = requests.get(full_url, timeout=5, allow_redirects=False)
            if res.status_code in [200, 401, 403]:
                findings.append({
                    "path": path,
                    "status": res.status_code,
                    "length": len(res.text),
                    "suspicious": True
                })
        except requests.RequestException:
            pass

    return findings
