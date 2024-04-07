from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to my simple web service!"

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/data')
def data():
    sample_data = {"name": "John", "age": 30, "city": "New York"}
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
