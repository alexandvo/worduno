from flask import Flask, jsonify, request
from openai import OpenAI
from flask_cors import CORS
from helpers.response_generator import getResponse
from dotenv import load_dotenv
import os
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import atexit

def self_ping():
    try:
        # Replace 'your-app-url' with the actual URL of your Render app
        requests.get("https://worduno-backend.onrender.com/")
        print("Self-ping successful")
    except Exception as e:
        print(f"Self-ping failed: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(func=self_ping, trigger="interval", minutes=0.1)
scheduler.start()

load_dotenv()

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

@app.route('/')
def refresh():
    return "Refreshing Inactivity."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT'))