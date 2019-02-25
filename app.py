# import flask dependencies
from flask import Flask 
from flask import jsonify
from flask import request
from flask import make_response

# initialize the flask app
app = Flask(__name__)

#def googleSearch(request):
#    response = GoogleSearch().search(request)
#    return {response}	

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    quaeryAction = req.get('queryResult').get('action')
    quaeryText = req.get('queryResult').get('queryText')
#   response = googleSearch(quaeryText)

    # return a fulfillment response!
    return {'fulfillmentText': quaeryText}	

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))	

# run the app
if __name__ == '__main__':
   app.run()