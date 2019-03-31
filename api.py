import flask
from flask import json
from flask import request

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/logs', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'application/json':
        # <send data to Kinesis>
        f = open('./logs', 'wb')
        f.write(request.data)
        f.close()
        return "JSON message: " + json.dumps(request.json)

    else:
        return "415 Unsupported Media Type"


app.run()
