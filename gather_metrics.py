import os

import requests

api_token = os.environ.get("VALOHAI_API_TOKEN")
project_id = os.environ.get("VH_PROJECT_ID")

resp = requests.request(
    url="https://staging.valohai.com/api/v0/executions/multi_download_metadata_csv/",
    method="POST",
    headers={"Authorization": f"Token {api_token}"},
    json={
        "environment": {"name": 'Staging AWS eu-west-1 p3.2xlarge', "owner": 'Valohai-internal',
                        "slug": 'staging-aws-eu-west-1-p3-2xlarge', "type": "vm"},
        "project": {"name": "drift-detection"},
        "status": "started",
        'runtime_config': {},
        "step": "train-model",

    }
)
if resp.status_code == 400:
    raise RuntimeError(resp.json())
resp.raise_for_status()
data = resp.json()
