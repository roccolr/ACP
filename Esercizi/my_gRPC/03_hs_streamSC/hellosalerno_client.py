import sys, hellosalerno_pb2_grpc, hellosalerno_pb2, grpc

def run(port):
    print('[CLIENT\t\t\tinizio]\n')

    with grpc.insecure_channel(f"localhost:{str(port)}") as channel:
        stub = hellosalerno_pb2_grpc.GreeterStub(channel=channel)

        for res in stub.sayHello(hellosalerno_pb2.HelloRequest(name="Broccolo")):
            print(f'[CLIENT]\t\t\tricevuta risposta res: {res.msg}\n')
        
        print('[CLIENT]\t\t\tfuori dal for\n')

if __name__ == '__main__':
    try: 
        PORT = int(sys.argv[1])
    except IndexError:
        print('ERRORE\t\t\tper favore specifica il port')
    
    run(PORT)

