import valkey

v = valkey.Valkey(host='localhost', port=6379, db=0)

def list_all_keys():
    stream_keys = map(lambda b: b.decode('utf-8'),v.scan(_type='STREAM', count=100)[1])
    for key in stream_keys:
        print(key)

def receive_sae_data():
    while True:
        try:
            data = v.xread(count=1, streams={'objecttracker:cam02': '>'}, block=2000)
            for item in data:
                proto_data = item[1][0][1][b'proto_data_b64']
                stream_key = item[0].decode('utf-8')
                print(proto_data, stream_key)
        except Exception as e:
            print("Error:", e)
            continue

#list_all_keys()
receive_sae_data()