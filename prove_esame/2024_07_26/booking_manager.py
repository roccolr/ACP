import stomp, requests, time

class ManagerListener(stomp.ConnectionListener):

    def __init__(self, conn):
        self.conn = conn

    def on_message(self, frame):
        # spacchetta la stringa

        msg = frame.body
        splitted_msg = msg.split('-')
        res = None
        if(splitted_msg[0] == 'create'):
            client = splitted_msg[1]
            hotel = splitted_msg[2]
            operator = splitted_msg[3]
            nights = splitted_msg[4]
            people = splitted_msg [5]
            cost = splitted_msg [6]

            json_to_send = {
                'client':client,
                'hotel':hotel,
                'operator':operator,
                'nights':nights,
                'people':people,
                'cost':cost
            }

            res = requests.post('http://127.0.0.1:5000/prenotazione', json= json_to_send)


        elif(splitted_msg[0] == 'update'):
            operator = splitted_msg[1]
            discount = splitted_msg[2]
            nights = splitted_msg[3]

            json_to_send = {
                'operator':operator,
                'discount':discount,
                'nights':nights
            }

            res = requests.put('http://127.0.0.1:5000/prenotazione', json= json_to_send)
        else:
            print('[MANAGER]\trichiesta non supportata')

        if (res.status_code == 200):
            print('[MANAGER]\trichiesta effettuata con successo')
            conn.send('/topic/response', 'Operazione effettuata con successo!')


if __name__ == '__main__':
    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait=True)

    conn.subscribe('/topic/request', id=1)
    conn.set_listener('Manager', ManagerListener(conn))

    try:
        time.sleep(60)
    except(KeyboardInterrupt):
        print('[MANAGER]\tsayonara')
    