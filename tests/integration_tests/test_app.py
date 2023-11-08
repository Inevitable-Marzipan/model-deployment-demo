import os
import json
import requests

def test_health_check():
    host = os.environ.get('HOST', 'http://localhost')
    url = f'{host}:8080/health_check'

    response = requests.get(url)

    assert response.status_code == 200
    assert json.loads(response.text) == {"success": True}


def test_score_with_sample_data():

    sample_file = 'data/sample_input.json'
    with open(sample_file, 'r') as f:
        sample_data = json.load(f)

    host = os.environ.get('HOST', 'http://localhost')
    url = f'{host}:8080/score'
    headers = {
            'Content-type': "application/json"
        }

    data = json.dumps(sample_data)
    response = requests.post(url, headers=headers, data=data)

    assert response.status_code == 200
    assert isinstance(json.loads(response.text), list)
