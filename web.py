from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Homepage"

@app.route('/about')
def about():
    return "About-Us"

@app.route('/data')
def data():
    sample_data = {"Name" : "John Doe", "Age" : 25, "City" : "New Jersey"}
    return jsonify(sample_data)

def __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
