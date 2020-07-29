from flask import Flask, request, jsonify
import requests
from config import TELEGRAM_WEBHOOK_URL
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Solve 405 Method Not Allowed (request method is known by the server but is not supported by the target resource.)

# this is wrong, suppose to post?
requests.get(TELEGRAM_WEBHOOK_URL)
print(requests)
#dummy function to test flask
@app.route('/webhook', methods=['GET'])
def check():
    return jsonify(success=True)

@app.route('/webhook', methods=['POST'])
def index():
    req = request.get_json()
    print(req['message'])
    return jsonify(success=True) # TODO: Success should reflect the success of the reply

if __name__ == '__main__':
    app.run(port=80)

