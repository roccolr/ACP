import helloworld_pb2, helloworld_pb2_grpc, grpc, sys

def generator():
    names = ["Giorgio", "Alessandro", "Marittiello", "Luca", "Amedeo"]
    for name in names:
        yield helloworld_pb2.HelloRequest(name = name)


def run(port):
    with grpc.insecure_channel(f"127.0.0.1:{str(port)}") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel=channel)

        

        # mandiamo un iteratore, riceviamo un iteratore
        res = stub.say_hello(generator())

        for r in res:
            print(f"[CLIENT]\tricevuto risposta: {r.msg}")

if __name__ == '__main__':
    try:
        port = sys.argv[1]
    except IndexError:
        print("[ERRORE]\tspecificare argomento port")

    run(port)

