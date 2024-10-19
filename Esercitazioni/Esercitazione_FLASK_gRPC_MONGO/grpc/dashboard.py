import statistics_pb2, statistics_pb2_grpc, grpc 

def run():
    with grpc.insecure_channel('127.0.0.1:6969') as channel:
        # ottengo i sensori 
        proxy = statistics_pb2_grpc.StatisticsManagerStub(channel)

        iterator = proxy.getSensors(statistics_pb2.Empty())
        sensors = []
        for item in iterator:
            sensors.append(item)
            print(f'[DASHBOARD]\t ricevuto sensore: {item.sensor_id}:{item.data_type}')

        # for i in range(0,5):
        #     print(str(sensors[i].sensor_id) + ' '+sensors[i].data_type)

        for sensor in sensors:
            sensor_id = int(sensor.sensor_id)
            data_type = sensor.data_type

            print(f'calcolo media: sensore_id {sensor_id}, data type: {data_type}')
            mean = proxy.getMean(statistics_pb2.MeanRequest(sensor_id=sensor_id, data_type=data_type))
            print(f'[STATISTICS]\t sensor: {sensor.sensor_id} - media: {mean}')

if __name__ == '__main__':
    run()