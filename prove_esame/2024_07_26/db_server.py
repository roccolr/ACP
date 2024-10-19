from flask import Flask, request
import pymongo

app = Flask(__name__)

def get_db():
    client = pymongo.MongoClient()
    db = client['gest_prenotazioni']
    return db

@app.post('/prenotazione')
def create():
    db = get_db()
    collection = db['prenotazioni']

    msg = request.get_json()

    collection.insert_one(msg)
    print('[SERVER]\tprenotazione inserita con successo')
    return ({"esito":"positivo"}, 200)

@app.put('/prenotazione')
def update():
    db = get_db()
    collection = db['prenotazioni']

    json_msg = request.get_json()
    operatore = json_msg['operator']
    nights = json_msg['nights']
    discount = int(json_msg['discount'])

    # query
    # collection.update_many({'operator':operatore, 'nights':{'$gte': nights}}, {'%set':{'cost':cost-discount}})
    query = {'operator':operatore, 'nights':{'$gte':nights}}

    results = collection.find(query)

    for result in results:
        _id = result['_id']
        costo = int(result['cost'])
        new_costo = costo-discount
        if(new_costo<0):
            new_costo = 0
        collection.update_one({'_id':_id}, {'$set':{'cost':str(new_costo)}})
        print('[SERVER]\tdocumento aggiornato con successo')
    
    return ({"esito":"positivo"}, 200)


if __name__ == '__main__':
    app.run()
    #default port = 5000
