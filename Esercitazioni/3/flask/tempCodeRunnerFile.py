def get_db():
    print('db invocato')
    client = pymongo.MongoClient()
    db = client['mydb1']
    return db