import json
from bottle import route, template, run
import os

# with open('last_transaction.json', 'w') as f:
#     f.write(json.dumps({"sender": "The Sewak", "amount": "100", "remarks": "Testing"}))
    


@route('/')
def index():
    try:
        with open('last_transaction.json', 'r') as f:
            lt = json.loads(f.read())
            sender = lt['sender']
            amount = lt['amount']
            remarks = lt['remarks']
    
        os.remove('last_transaction.json')

    except:
        sender = ''
        amount = ''
        remarks = ''


    return template('index.html', sender=sender, amount=amount, remarks=remarks)


if __name__ == '__main__':
    run(host='localhost', port=8000)
