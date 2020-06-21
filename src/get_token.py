from datetime import datetime, timedelta
import jwt
import os
import requests


def get_private_pem():
    key = os.getenv("PRIVATE_KEY")

    return key


def make_auth_header(installation_id):
    utcnow = datetime.utcnow() + timedelta(seconds=-5)
    duration = timedelta(seconds=30)
    payload = {
        "iat": utcnow,
        "exp": utcnow + duration,
        "iss": os.getenv("APP_ID")
    }
    pem = get_private_pem()
    encoded = jwt.encode(payload, pem, "RS256")
    headers = {
        "Authorization": "Bearer " + encoded.decode("utf-8"),
        "Accept": "application/vnd.github.machine-man-preview+json"
        }

    auth_url = f"https://api.github.com/installations/{installation_id}/access_tokens"
    r = requests.post(auth_url, headers=headers)

    if not r.ok:
        print(r.json()['message'])
        r.raise_for_status()
    token = r.json()['token']
    with open('token.conf', 'w') as f:
        f.write(token)
    return {
        'Authorization': f'token {token}',
    }


if __name__ == '__main__':
    installation_id = os.getenv('INSTALLATION_ID')
    make_auth_header(installation_id)
