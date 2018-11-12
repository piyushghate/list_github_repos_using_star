from flask import Flask, jsonify, request
# from test_flask_with_main import *
from main_api import run_api

app = Flask(__name__)


@app.route('/repo', methods = ['POST'])
def index():
    if(request.method == 'POST'):
        input_json = request.get_json()
        return_from_mainapp = run_api(input_json)
        return jsonify({'results': return_from_mainapp}), 201

if __name__ == '__main__':
    app.run(debug=True)