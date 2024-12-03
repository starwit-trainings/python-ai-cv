import time

import valkey


STREAM_NAME = 'geomapper:stream1'

v = valkey.Valkey(host='localhost', port=6379, db=0)

def list_all_keys():
    stream_keys = map(lambda b: b.decode('utf-8'),v.scan(_type='STREAM', count=100)[1])
    for key in stream_keys:
        print(key)

def receive_sae_data():
    while True:
        try:
            data = v.xread(count=1, streams={STREAM_NAME: '$'}, block=1000)
            print(f'\n============ NEW QUERY RESULT ==============\n')
            print(data)
        except Exception as e:
            print("Error:", e)
            time.sleep(0.2)
            continue

list_all_keys()
receive_sae_data()