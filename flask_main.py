from flask import Flask, jsonify, request
from test_flask_with_main import *

app = Flask(__name__)


@app.route('/repo', methods = ['POST'])
def index():
    if(request.method == 'POST'):
        input_json = request.get_json()
        return_from_mainapp = run_api(input_json)
        return jsonify({'results': return_from_mainapp}), 201
    else:
        return jsonify({"about" : "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)