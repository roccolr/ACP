from flask import Flask, request
import pymongo

app = Flask(__name__)

def get_db() -> pymongo.database.Database:
    '''
    ritorna una connessione al db, da invocare all'interno delle view functions
    '''
    client = pymongo.MongoClient('127.0.0.1', 27017)
    return client['operations_db']

@app.post('/sensor')
def add_sensor():
    db = get_db()
    sensors = db['sensors'] #collection dei sensori

    # la richiesta è strutturata tipo {'_id':intero, 'data_type':'temp'or'press'}

    id = request.get_json()['_id'] #intero
    data_type = request.get_json() ['data_type'] #stringa

    try:
        sensors.insert_one({'_id':id, 'data_type':data_type})
    except Exception:
        print("Errore durante l'inserimento nel db del sensore")
        return ({'result':'error'}, 505)
    else:
        print(f"[Controller]\tInserito nel db il sensore con _id: {id}\tdata_type:{data_type}")
        return {'result':'success'}


@app.post('/data/<data_type>') #nell'URL viene specificato se si tratta di una rilevazione temp o press
def add_measure(data_type):
    db = get_db()

    if (data_type == 'temp'):
        temp_data = db['temp_data']
        sensor_id = request.get_json()['sensor_id']
        data = request.get_json()['data']

        temp_data.insert_one({'sensor_id':sensor_id, 'data':data})
        print(f'[CONTROLLER]\tricevuto dato temp: {data}\tsensore: {sensor_id}')
        return {'resutl':'success'}
    elif (data_type == 'press'):
        press_data = db['press_data']
        sensor_id = request.get_json()['sensor_id']
        data = request.get_json()['data']

        press_data.insert_one({'sensor_id':sensor_id, 'data':data})
        print(f'[CONTROLLER]\tricevuto dato press: {data}\tsensore: {sensor_id}')
        return {'result':'success'}
    else:
        print(f'[CONTROLLER]\t404, not found!')
        return ({'result':'error'}, 404)

if __name__ == '__main__':
    app.run()


