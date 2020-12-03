from flask import request, Flask
import json

server2 = Flask(__name__)
@server2.route('/')
def home():
    return '<h1>Hello AsiaYo 2</h1>'

if __name__ == '__main__':
    server2.run(debug = True, host = '0.0.0.0')
