import grpc, statistics_pb2, statistics_pb2_grpc


if __name__ == '__main__':
    with grpc.insecure_channel('127.0.0.1:6969') as channel:
        stub = statistics_pb2_grpc.statisticsStub(channel=channel)

        sensors = stub.get_sensor(statistics_pb2.Empty())

        
        for sensor in sensors:
            _id = sensor._id
            data_type = sensor.data_type

            mean = stub.get_mean(statistics_pb2.Mean_Request(sensor_id=_id, data_type=data_type))
            print(f'[DASHBOARD]\tsensore {_id}, media: {mean}')


