from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods = ['POST'])
def index():
    if(request.method == 'POST'):
        input_json = request.get_json()
        return jsonify({'you sent': input_json}), 201
    else:
        return jsonify({"about" : "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)