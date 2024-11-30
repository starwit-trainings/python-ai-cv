import valkey
from time import sleep

v = valkey.Valkey(host='localhost', port=6379, db=0)

def receive_data():
    result = v.xread(count=1, block=2000, streams={'data_stream':'$'})
    for item in result:
        print(item)


if __name__ == "__main__":
    while True:
        receive_data()
        sleep(1)