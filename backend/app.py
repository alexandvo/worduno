from flask import Flask, jsonify, request
from openai import OpenAI
from flask_cors import CORS
from helpers.response_generator import getResponse
from dotenv import load_dotenv
import os
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

load_dotenv()

def my_scheduled_task():
    print("Refreshing Inactive Cooldown")

scheduler = BackgroundScheduler()
scheduler.add_job(func=my_scheduled_task, trigger="interval", minutes=5)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

api_key = os.getenv('OPEN_AI_API_KEY')

client = OpenAI(api_key=api_key)

app = Flask(__name__)
CORS(app, resources={r"/simplify": {"origins": "chrome-extension://bhoglaohnjphilfenndhbhekclfijlhm"}})

@app.route('/simplify', methods=['POST'])
def getSimplifiedText():
    if request.method == 'POST':
        message = request.json.get('message')
        if message != "":
            res = getResponse(client, message)
            return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT'))