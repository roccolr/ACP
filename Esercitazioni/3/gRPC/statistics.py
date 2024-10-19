import grpc, statistics_pb2, statistics_pb2_grpc, pymongo
from concurrent import futures

def get_db():
    # print('db invocato')
    client = pymongo.MongoClient()
    db = client['mydb1']
    return db

class Statistics(statistics_pb2_grpc.statisticsServicer):
    def get_sensor(self, request, context):
        db = get_db()
        collection = db['sensors']
        query_res = collection.find()

        for doc in query_res:
            yield statistics_pb2.Sensors(_id=int(doc['_id']), data_type=doc['data_type'])

    def get_mean(self, request:statistics_pb2.Mean_Request, context):
        db = get_db()
        collection = None
        sensor_id = request.sensor_id
        data_type = request.data_type

        if(data_type == 'temp'):
            collection = db['temp_data']
        elif (data_type == 'press'):
            collection = db['press_data']
        else:
            print('[STATISTICS]\terrore nella lettura')
        
        query_res = collection.find({'sensor_id':sensor_id})
        misure = []
        for doc in query_res:
            misure.append(doc['data'])
        
        sum = 0
        for m in misure:
            sum+=m
        avg = 0
        try:
            avg = sum/len(misure)
            return (statistics_pb2.StringMessage(mean=str(avg)))
        except ZeroDivisionError:
            return (statistics_pb2.StringMessage(mean="Errore"))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(5))
    port = server.add_insecure_port('127.0.0.1:6969')
    statistics_pb2_grpc.add_statisticsServicer_to_server(Statistics(), server)
    try:
        server.start()
        print(f'[STATISTICS SERVER]\t running on localhost:{port}')
        server.wait_for_termination()
    except KeyboardInterrupt:
        print('[STATISTICS SERVER]\tinterrotto manualmente')
    

if __name__ == '__main__':
    serve()
    
