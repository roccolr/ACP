from flask import Flask, request
import pymongo

app = Flask(__name__)

def get_db():
    print('db invocato')
    client = pymongo.MongoClient()
    db = client['mydb1']
    return db

@app.post('/sensor')
def create_sensor():
    # print('debug')
    db = get_db()
    collection = db['sensors']
    json_req = request.get_json()
    _id = json_req['_id']
    data_type = json_req['data_type']

    print(f'[CONTROLLER]\tricevuta post request, contenuto _id:{_id}, data_type:{data_type}')

    res = collection.insert_one(json_req)
    if(not(res.acknowledged)):
        return {'result':'fail'}
    return {'result':'success'}, 200

@app.post('/sensor/<data_type>')
def create_data(data_type:str):
    db=get_db()
    collection = None
    if (data_type == 'temp'):
        collection = db['temp_data']
    elif(data_type == 'press'):
        collection = db['press_data']
    else:
        return {'result':'fail'}, 505
    
    json_req = request.get_json()
    sensor_id = json_req['sensor_id']
    data = json_req['data']
    print(f'[CONTROLLER]\tricevuta post request, contenuto sensor_id:{sensor_id}, data:{data}')

    res = collection.insert_one(json_req)

    if(not(res.acknowledged)):
        return {'result':'fail'}
    return {'result':'success'}

if __name__ =='__main__':
    app.run()
