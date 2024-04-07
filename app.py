from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello & Welcome to Another Fail of The Year"

@app.route("/home")
def index():
    return "This is the homepage"

@app.route("/data")
def data():
    sample_data = {"Name" : "Dewa", "Age" : 19, "Class" : "LC01"}
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

