from flask import Flask, request
import uuid

app = Flask(__name__)

#creazione del dizionario dove verranno conservati i valori
notes = {}


@app.post('/note')
def add_note():

    # riceviamo una richiesta di tipo POST il cui corpo è un file di tipo JSON
    
    try:
        text = request.get_json()['text']
        tag = request.get_json()['tag']
    except KeyError:
        print(f'[ADD]\tbad format')
        return {'result':'error bad format', 'id':-1}
    else:
        print("[ADD]\treceived note:", text, "with tag:", tag)

        id = uuid.uuid4().hex
        print(f'ID: {id}')
        notes[id] = request.get_json()

        return {'result':'added', 'id':id}


@app.get('/note/<id>')
def get_note(id):
    print(f'[GET NOTE]\trecieved id: {id}')

    try:
        note = notes[id]
    except KeyError:
        print(f'[GET NOTE]\tNote not found')
        return {'result':'note not found'}, 404
    else:
        print(f'[GET NOTE]\tritorno nota con codice: {id}')
        return note

@app.get('/notes')
def get_notes():
    print("[GET NOTES] Received request")
    result = []

    for id,note in notes.items():
        result.append({"id":id, "note":note})
    
    return result

@app.put('/note/<id>')
def update_note(id):
    print(f"[UPDATE] Received request for id: {id}")

    try:
        text = request.get_json()["text"]
        tag = request.get_json()["tag"]
    except KeyError:
        print("[GET NOTES]bad format")

    try:
        print(f'TEST\t{notes[id]}')
    except KeyError:
        print('[UPDATE]\t404 not found')
        notes[id] = request.get_json()
        return {'result':'new one created','note':notes[id]}

    notes[id]=request.get_json()
    print("[GET NOTES]\tUpdated...")
    return {'result':'updated', 'note':notes[id]}

@app.delete('/note/delete')     #arriverà un url del tipo http://127.0.0.1:6969/delete?id=codicecodice
def delete_note():

    try:    
        params = request.args
        id = args["id"]
        print(f'[DELETE] Receive request for id: {id}')

        notes.pop(id)
    except KeyError:
        print(f'[DELETE]\tNote not found')
        return {'result':'Note not found'}, 404
    
    return {'result':'deleted', 'id':id}, 200

@app.delete('/note/notes')
def delete_notes():
    notes.clear()
    return {'result':'no_more_notes'}


if __name__ == '__main__':
    app.run('127.0.0.1', 6969)

        
