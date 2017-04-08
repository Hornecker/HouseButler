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

    # Build JSON result
    res = processRequest(req)
    res = json.dumps(res, indent=4)

    # Make response complient including json header
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'

    return r


def processRequest(req):
    if req.get("result").get("action") != "controlLight":
        return {}

    # Action for controlling light received
    baseurl = "http://5.186.52.135:1000/webhook/"
    
    params = urllib.urlencode({'number': 12524, 'type': 'issue', 'action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(baseurl)
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    
    return
    {
        "speech": "speech here",
        "displayText": "speech here",
        "source": "apiai-mybutler-lightcontrol-webhook"
    }


def makeQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")

    return "weather.forecast"


def makeWebhookResult(data):
    return
    {
        "speech": "speech here",
        "displayText": "speech here",
        "source": "apiai-mybutler-lightcontrol-webhook"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
