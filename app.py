# import flask dependencies
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from googleapiclient.discovery import build
import json
import requests

# initialize the flask app
app = Flask(__name__)

my_api_key = "AIzaSyAL-FNUcVnrxThJO5JEwz_VPxzqRJnjbJo"
my_cse_id = "016982423635796478701:vbd7wfy6qei"

def google_search_txt(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items'][0]['link']

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    quaeryAction = req.get('queryResult').get('action')
    quaeryText = req.get('queryResult').get('queryText')

    # return a fulfillment response!
    return {'fulfillmentText': google_search_txt(quaeryText, my_api_key, my_cse_id, num=3)}	

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()