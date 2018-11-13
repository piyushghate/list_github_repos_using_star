from flask import Flask, jsonify, request
from main_api import run_api        # importing the api fucntion

app = Flask(__name__)


@app.route('/repos', methods = ['POST'])    # defines the method and path to the api
def index():
    if(request.method == 'POST'):
        return_from_mainapp = run_api(request.get_json())
        return jsonify({'results': return_from_mainapp}), 201

if __name__ == '__main__':
    app.run(debug=True)