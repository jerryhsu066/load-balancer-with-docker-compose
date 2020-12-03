from flask import request, Flask
import json

server1 = Flask(__name__)
@server1.route('/')
def home():
    return '<h1>Hello AsiaYo 1</h1>'

@server1.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    server1.run(debug = True, host = '0.0.0.0')
