import stomp
import matplotlib.pyplot as plt
import numpy as np
import time

class TempAnalyzerListener(stomp.ConnectionListener):

    def __init__(self, q:list):
        self.q = q

    def on_message(self, frame:stomp.utils.Frame):
        msg = frame.body
        q.append(int(msg))
        print(f"[ANALYZER]\tricevuto valore: {msg} e inserito in coda. len(q)= {len(q)}")

        if(len(q) == 20):
            plt.plot(q)
            # plt.show()
            plt.savefig("/home/studente/Desktop/acp/prove_esame/2023_09_08/figura/immagine.png")
            q.clear()


if __name__ == '__main__':
    conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
    # stomp.transport.Transport()
    q = []
    conn.connect(wait=True)
    conn.subscribe('/topic/tempTopic', id=1)
    conn.set_listener("temp_analyzer", TempAnalyzerListener(q))

    try:
        while(True):
            time.sleep(1)
    except KeyboardInterrupt:
        print("Sayonara")

    

