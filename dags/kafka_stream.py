import uuid
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args ={
    'owner':'airscholar',
    'start_date':datetime(2024, 6, 29, 22, 00)
}

def get_data():
    import requests
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = str(location['street']['number']) + ' ' + str(location['street']['name'])+ ', ' + str(location['city']) + ', ' + str(location['state']) +', ' +str(location['country']) + ', ' + str(location['postcode'])
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['picture'] = res['picture']['medium']
    return data

def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging
    import six
    import sys
    if sys.version_info >= (3, 12, 0):
        sys.modules['kafka.vendor.six.moves'] = six.moves

    #print(json.dumps(res, indent=3))
    current_time = time.time()
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)

    while True:
        if time.time() > current_time + 30:
            break
        try:
            res = get_data()
            res = format_data(res)
  
            producer.send('users_created',json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue

with DAG('user_automation',
default_args=default_args,
schedule_interval='@daily',
catchup=False) as dag:
    streaming_task = PythonOperator(
        task_id = 'stream_data_from_api',
        python_callable=stream_data
    )

