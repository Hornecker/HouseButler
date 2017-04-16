#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)
    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    
    return r


def processRequest(req):
    if req.get("result").get("action") != "controlLight":
        return {}

    result = req.get("result")
    parameters = result.get("parameters")

    # Collect light control data
    state = parameters.get("boolean-type")
    room = parameters.get("location-type")
    subject = parameters.get("subject-type")

    state = state.replace(' ', '-')
    room = room.replace(' ', '-')
    subject = subject.replace(' ', '-')

    url = "http://5.186.52.135:1000/webhook?state=" + state + "&room=" + room + "&subject=" + subject
    result = urlopen(url).read()

    # Building response to API.AI backend
    speech = json.dumps(result, indent=4)

    response = { "speech": speech, "displayText": speech, "source": "apiai-mybutler-lightcontrol" }
    return response

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')