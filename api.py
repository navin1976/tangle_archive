#!flask/bin/python
from flask import Flask
import urllib2
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to IOTA API"

@app.route('/put/<string:hash>')
def post(new):
    bundle = hash

command = {
    'command': 'getTransactionsToApprove',
    'depth': 27
}

stringified = json.dumps(command)

headers = {
    'content-type': 'application/json',
    'X-IOTA-API-Version': '1'
}

request = urllib2.Request(url="http://node.deviceproof.org:14265", data=stringified, headers=headers)
returnData = urllib2.urlopen(request).read()

jsonData = json.loads(returnData)

command = {
    'command': 'attachToTangle',
    'trunkTransaction': jsonData["trunkTransaction"], 
    'branchTransaction': jsonData["branchTransaction"],
    'minWeightMagnitude': 18,
    'trytes': hash
}

stringified = json.dumps(command)

headers = {
    'content-type': 'application/json',
    'X-IOTA-API-Version': '1'
}

request = urllib2.Request(url="http://node.deviceproof.org:14265", data=stringified, headers=headers)
returnData = urllib2.urlopen(request).read()

jsonData = json.loads(returnData)

command = {
    'command': 'broadcastTransactions',
    'trytes': jsonData["trytes"]
}

stringified = json.dumps(command)

headers = {
    'content-type': 'application/json',
    'X-IOTA-API-Version': '1'
}

request = urllib2.Request(url="http://node.deviceproof.org:14265", data=stringified, headers=headers)
returnData = urllib2.urlopen(request).read()

jsonData = json.loads(returnData)


if __name__ == "__main__":
    app.run(debug=True)