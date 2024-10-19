import sys, hellosalerno_pb2, hellosalerno_pb2_grpc, grpc


#creiamo un generatore 
def generatore_richieste():
    nomi = ['Rocco', 'Broccolo', 'Brock']
    for n in nomi:
        yield hellosalerno_pb2.helloRequest(nome=n)

def run(port):
    with grpc.insecure_channel(f'localhost:{int(port)}') as channel:
        print(f'[CLIENT]\t\t\t connesso a localhost:{int(port)}')
        stub = hellosalerno_pb2_grpc.GreeterStub(channel)
        
        res = stub.sayHello(generatore_richieste())

        print(f'[CLIENT]\t\t\tRicevuto in risposta: {res.msg}')


if __name__ == '__main__':
    try:
        PORT = int(sys.argv[1])
    except IndexError:
        print('ERRORE\t\t\tindicare porto')
    run(PORT)
        



