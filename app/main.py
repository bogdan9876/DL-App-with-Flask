from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({'result': 1})


if __name__ == '__main__':
    app.run()
