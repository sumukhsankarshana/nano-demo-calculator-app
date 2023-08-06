from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello World!", 200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    num1 = data['first']
    num2 = data['second']
    result = int(num1) + int(num2)
    return jsonify({"result": result}), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data['first']
    num2 = data['second']
    result = int(num1) - int(num2)
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
