import grpc
import hellosalerno_pb2_grpc
import hellosalerno_pb2

def run():
    # creiamo il canale grpc pythonicamente

    with grpc.insecure_channel("localhost:50051") as channel:
        # usiamo questa variabile channel come input del proxy/stub lato client
        stub = hellosalerno_pb2_grpc.GreeterStub(channel=channel)

        # si invoca il metodo dallo stub e si conserva il valore restituito in una variabile
        res = stub.SayHello(hellosalerno_pb2.HelloRequest(name= "BROCCOLO"))

        print("type(resp) : ", type(res))

        print("[CLIENT] Risposta dopo SayHello(): " + str(res.message))


if __name__ == '__main__':
    run()