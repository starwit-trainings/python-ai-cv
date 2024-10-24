from concurrent import futures
import logging
import time
import grpc
from google.protobuf.timestamp_pb2 import Timestamp
import football_manager_pb2_grpc
import football_manager_pb2

class FootballService(football_manager_pb2_grpc.FootballServiceServicer):

    data = [{"id": 1,
            "name": "FC Bayern Muenchen",
            "league_id": 1},
            {"id": 2,
            "name": "VfL Wolfsburg",
            "league_id": 1}]

    def __init__(self):
        logging.info("server created")    

    def GetClubs(self, request, context):
        result = []
        for club in self.data:
            resp = football_manager_pb2.ClubResponse(id=club["id"], name=club["name"], league_id=club["league_id"])
            result.append(resp)
        return football_manager_pb2.ClubList(clubs=result)

    def GetClub(self, request, context):
        result = next((club for club in self.data if club["id"] == request.id), None)
        if result:
            return football_manager_pb2.ClubResponse(id=result["id"], name=result["name"], league_id=result["league_id"])
        
    def GeLiveData(self, request, context):
        for i in range(5):
            yield football_manager_pb2.LiveTickerResponse(update_time=Timestamp())
            time.sleep(0.5)
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    football_manager_pb2_grpc.add_FootballServiceServicer_to_server(FootballService(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()