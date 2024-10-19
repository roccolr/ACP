from flask import Flask, request 

app = Flask(__name__)


@app.post('/update_history')
def update():
    json_msg = request.get_json()

    operation = json_msg['operation']
    serial_number = json_msg['serial_number']

    with open('/home/studente/Desktop/acp/prove_esame/2024_06_26/history.txt', 'a') as file:
        file.write(operation+'-'+serial_number+'\n')
    
    return {'result':'ok'}, 200

if __name__ == '__main__':
    app.run()