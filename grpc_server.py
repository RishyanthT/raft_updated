import grpc
from concurrent import futures
import time
import service_pb2
import service_pb2_grpc

class NodeCommunicationService(service_pb2_grpc.NodeCommunicationServicer):
    def SendEvent(self, request, context):
        # Process the event from the node
        print(f"Received event from node {request.id}: {request.type}, term: {request.term}")
        return request  # Echo back the received message as a response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_NodeCommunicationServicer_to_server(NodeCommunicationService(), server)
    server.add_insecure_port('[::]:50051')  # Listen on port 50051
    server.start()
    print("gRPC server is running on port 50051...")
    try:
        while True:
            time.sleep(86400)  # Run for one day
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
