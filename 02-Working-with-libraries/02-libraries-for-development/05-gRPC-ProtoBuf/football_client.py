import logging
import grpc

import football_manager_pb2
import football_manager_pb2_grpc
from google.protobuf import empty_pb2 

def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = football_manager_pb2_grpc.FootballServiceStub(channel)
        req = empty_pb2.Empty()
        resp = stub.GetClubs(req)
        print(resp)
        req = football_manager_pb2.ClubRequest(id=2)
        resp = stub.GetClub(req)
        print(resp)

        for ticker in stub.GeLiveData(req):
            print(ticker)


if __name__ == '__main__':
    logging.basicConfig()
    run()