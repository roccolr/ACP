from pymongo import MongoClient

def get_db():
    client = MongoClient('127.0.0.1', 27017)
    return client["test"]

def insert_items(db):
    item1 = {
        "nome":"Rocco",
        "cognome":"Lo Russo",
        "profesisone":"spazzacamino"
    }
    item2 = {
        "nome":"Giovanni",
        "cognome":"Giorgio",
        "professione":"producer"
    }

    db.insert_many([item1, item2])


if __name__ == '__main__':
    db_name = get_db()
    collection = db_name['anagrafica']
    insert_items(collection)
    

