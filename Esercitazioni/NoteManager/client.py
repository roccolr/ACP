import requests
import random


notes = {}
tags = ['work', 'sport']
server_address = 'http://127.0.0.1:6969'

def genera_nota():
    text = "nota_"+str(random.randint(1,100))

    tag = tags[random.randint(0,1)]

    return {"text":text, "tag":tag}

def get_random_note_id():

    key_list = list(notes.keys())
    list_len = len(key_list)

    res = key_list[random.randint(0, list_len-1)]

    return res


def add_note(note):

    res = requests.post(server_address+'/note', json=note)
    # è un response object, non un json. Ha anche un header

    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"ERRORE...{res.status_code}")
        return -1
    
    notes[res.json()["id"]] = note #creo la entry nel dizionario locale
    
    

def get_note(id):

    res = requests.get(server_address+'/note/'+id)

    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"[ERRORE]...{res.status_code}")
        return -1
    else:
        notes[id] = res.json()
        return res.json()

def get_notes():

    res = requests.get(server_address+'/notes')

    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f'ERRORE...{res.status_code}')
        return -1
    else:
        notes_result = res.json()
        for note in notes_result:
            notes[note["id"]] = note['note']
    
    return notes_result


def update_note(note, id): #note è il valore di nota che vogliamo aggiornare, id è l'identificativo 

    res = requests.put(server_address+'/note/'+str(id), json=note)

    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"[ERROR]\t{res.status_code}")
        return -1
    else:
        notes[str(id)] = res.json["note"]
        return res.json()["id"]
    

def delete_note(id):

    res = requests.delete(server_address+'/note', id=str(id))

    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print("[ERRORE]\t"+res.status_code)
    else:
        resp_json = res.json()
        notes.pop(resp_json["id"])
        return resp_json["id"]

def delete_notes():

    res = requests.delete(server_address+'/notes')

    try:
        res.raise_for_status
    except requests.exceptions.HTTPError:
        print(res.status_code)
    else:
        notes.clear()
        print(notes)
        return 0


if __name__ == '__main__':

    for i in range(0,2):
        note = genera_nota()
        add_note(note)

    id = get_random_note_id()
    
    print(get_notes())

    
