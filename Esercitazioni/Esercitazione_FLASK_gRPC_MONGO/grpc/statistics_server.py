import statistics_pb2, statistics_pb2_grpc, pymongo, grpc
from concurrent import futures

def get_db() -> pymongo.database.Database:
    client = pymongo.MongoClient('127.0.0.1', 27017)
    return client['operations_db']

def avgg(interi:list)->float:
    sum = 0
    for i in interi:
        sum+=i
    return (sum)/len(interi)

class Statistics_Manager(statistics_pb2_grpc.StatisticsManagerServicer):
    def getSensors(self, request, context):
        db = get_db()
        sensor_collection = db['sensors']
        sensor_cursor = sensor_collection.find({})

        # print(sensor_cursor)

        for sensor in sensor_cursor:
            print(sensor)
            yield (statistics_pb2.Sensor(sensor_id=int(sensor['_id']), data_type=sensor['data_type']))
        # print(f'[STATISTICS]\tgetSensors dal db effettuata con successo')
        # for sensor in sensor_cursor:
        #     try:
        #         print(f'[STATISTICS]\t yelding {sensor["_id"]} : {sensor["data_type"]}')
        #     except Exception:
        #         print(f'ERRORE durante la query, campo non presente')
        #         continue
        #     yield (statistics_pb2.Sensor(sensor_id= sensor['_id'], data_type= sensor['data_type']))


    def getMean(self, request, context):
        data_type = request.data_type
        sensor_id = request.sensor_id
        print(sensor_id, type(sensor_id), data_type)
        db = get_db()
        collection = None
        if (data_type == 'press'):
            collection = db['press_data']
            print('ottenuta la collection press')
        elif (data_type == 'temp'):
            collection = db['temp_data']
            print('ottenuta la collection temp')

        else:
            print('[DONT BE MEAN]')
        
        # print(collection.name)

        data = collection.find({"sensor_id":sensor_id})
        print(f'query effettuata con successo ')
        
        
        measures = []
        for d in data:
            measures.append(d['data'])
            print(d['data'])
        
        print(measures)
        
        return statistics_pb2.StringMessage(value= str(avgg(measures)))
        # return statistics_pb2.StringMessage(value='ciao')

def serve():
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(10))
    server.add_insecure_port('127.0.0.1:6969')
    statistics_pb2_grpc.add_StatisticsManagerServicer_to_server(Statistics_Manager(), server)
    server.start()
    print(f'[STATISTICS SERVER]\tstarted on port 6969')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

