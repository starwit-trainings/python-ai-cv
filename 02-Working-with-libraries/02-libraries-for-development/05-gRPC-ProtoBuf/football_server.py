from concurrent import futures
import logging
import grpc
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
        # Implement the logic to retrieve a specific club
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    football_manager_pb2_grpc.add_FootballServiceServicer_to_server(FootballService(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()