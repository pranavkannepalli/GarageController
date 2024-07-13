from flask import Flask, request, jsonify
import gpiozero
from time import sleep

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the Garage Controller API"

@app.route("/door", methods=["POST"])
def post():
    print("POST request made")
    content = request.json
    doorNum = content["doorNum"]
    print(doorNum)

    relay = gpiozero.OutputDevice(doorNum + 1, active_high=False)
    relay.off()
    sleep(1)
    relay.on()
    sleep(1)
    relay.off()
    sleep(1)

    return jsonify({"status": f"Opened relay number {doorNum}"})

if __name__ == "__main__":
    app.run()