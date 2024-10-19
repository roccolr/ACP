import stomp
import pymongo
import time

def get_db() -> pymongo.database.Database:
    client = pymongo.MongoClient()
    return client['analyzerdb']

class PressAnalyzerListener(stomp.ConnectionListener):
    def __init__(self):
        self.db = get_db()
        self.i = 0

    def on_message(self, frame:stomp.utils.Frame):
        msg = frame.body
        db = get_db()
        data_collection = db["pressure_data"]
        data_collection.insert_one({"_id":self.i, "value":int(msg)})
        self.i = self.i + 1
        print(f"[ANALYZER]\tricevuto valore: {msg} e inserito nel db")


if __name__ == '__main__':
    conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
    # stomp.transport.Transport()
    conn.connect(wait=True)
    conn.subscribe('/topic/pressTopic', id=2)
    conn.set_listener("analyzer", PressAnalyzerListener())

    try:
        while(True):
            time.sleep(1)
    except KeyboardInterrupt:
        print("Sayonara")

    

