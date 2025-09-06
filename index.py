from flask import Flask, request, jsonify
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response
import json

flask_app = Flask(__name__)

@flask_app.route("/", methods=["GET"])
def home():
    return "🚀 Flask API running on Vercel!"

@flask_app.route("/signal", methods=["POST"])
def signal():
    data = request.get_json()
    pair = data.get("pair", "N/A")
    timeframe = data.get("timeframe", "1m")
    return jsonify({
        "pair": pair,
        "timeframe": timeframe,
        "signal": "CALL",
        "confidence": "6/7 bullish vs 1/7 bearish"
    })

# Vercel entrypoint
def handler(environ, start_response):
    return DispatcherMiddleware(flask_app)(environ, start_response)
