import requests
import uuid
from datetime import datetime
import json
import valkey
import uuid
from time import sleep

v = valkey.Valkey(host='localhost', port=6379, db=0)
v.ping()
v.lpush('test', 'test')

def measure_response_time():
    url = "http://heise.de"
    response = requests.post(url)
    return response.elapsed.total_seconds()

def send_new_data():
    data_package = {}
    data_package['id'] = str(uuid.uuid4())
    data_package['resp_time'] = measure_response_time()
    data_package['ts'] = datetime.utcnow().isoformat()
    print(f"Sending message {data_package['id']}")
    v.xadd('data_stream', {'data': json.dumps(data_package)})
    sleep(1)


if __name__ == "__main__":
    for i in range(10):
        send_new_data()
