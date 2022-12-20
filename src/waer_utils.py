import json
import uuid
import requests
import pandas as pd
from google.cloud import storage


def get_auth_url():
    response = requests.post('https://api.tryterra.co/v2/auth/authenticateUser', headers={
        'accept': 'application/json',
        'content-type': 'application/json',
        'dev-id': 'waer-U40516NESV',
        'x-api-key': 'a639615c4991764f9dba6ab9a7b711a3bf1f971aaa2ff561edc13fd2f8f8311c'
    }, json={
       'resource': 'GARMIN',
       'auth_success_redirect_url': 'https://test-sgonnekoiq-uc.a.run.app/panel/success',
       'auth_failure_redirect_url': 'https://test-sgonnekoiq-uc.a.run.app/panel/failure'
    })
    return response.json()['auth_url']


def write_to_storage(data):
    storage_client = storage.Client(project='waer-370612')
    bucket = storage_client.get_bucket('waer-data')
    blob = bucket.blob('-'.join([data['user']['user_id'], data['type'], str(uuid.uuid4()).replace('-','')]))
    with blob.open(mode='w') as f:
        f.write(json.dumps(data))


def call_data_api(user_id):
    for dtype in ['daily', 'activity', 'athlete', 'sleep', 'body']:
        #print(dtype)
        #for beg in pd.date_range('2020-01-01','2022-12-20'):
        for beg in [pd.to_datetime('2020-01-01')]:
            end = beg + pd.offsets.DateOffset(days=365*3)
            beg_date = str(beg.date())
            end_date = str(end.date())
            
            url = f'https://api.tryterra.co/v2/{dtype}?user_id={user_id}&start_date={beg_date}&end_date={end_date}&to_webhook=true&with_samples=true'
            response = requests.get(url, headers={
                'accept': 'application/json',
                'dev-id': 'waer-U40516NESV',
                'x-api-key': 'a639615c4991764f9dba6ab9a7b711a3bf1f971aaa2ff561edc13fd2f8f8311c'
            })
            if response.status_code!=200:
                print(f'FAILURE WHEN CALLING {url}')


def call_user_id_api():
    url = "https://api.tryterra.co/v2/subscriptions"
    response = requests.get(url, headers={
        'accept': 'application/json',
        'dev-id': 'waer-U40516NESV',
        'x-api-key': 'a639615c4991764f9dba6ab9a7b711a3bf1f971aaa2ff561edc13fd2f8f8311c'
    })
    print([i for i in map(lambda x: x['user_id'], response.json()['users'])])


def call_deactivate_api(user_id):
    url = f"https://api.tryterra.co/v2/auth/deauthenticateUser?user_id={user_id}"
    response = requests.delete(url, headers={
        'accept': 'application/json',
        'dev-id': 'waer-U40516NESV',
        'x-api-key': 'a639615c4991764f9dba6ab9a7b711a3bf1f971aaa2ff561edc13fd2f8f8311c'
    })
    print(response.json())
