import hellosalerno_pb2, hellosalerno_pb2_grpc, sys, grpc

#generatore da passare al server
def generatore_richieste():
    nomi = ['Rocco', 'Broccolo', 'Brock']
    for n in nomi:
        yield hellosalerno_pb2.helloRequest(nome=n)

def run(port):
    with grpc.insecure_channel(f'localhost:{port}') as channel:
        stub = hellosalerno_pb2_grpc.GreeterStub(channel=channel)

        res = stub.sayHello(generatore_richieste())

        for r in res:
            print(f'[CLIENT]\t\t\tRicevuto: {r.msg}')
        
        print('[CLIENT]\t\t\tFINE')

if __name__ == '__main__':
    try:
        PORT = int(sys.argv[1])
    except IndexError:
        print('ERRORE\t\t\tspecificare porto')
    
    run(PORT)