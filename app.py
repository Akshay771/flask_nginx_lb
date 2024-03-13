from flask import Flask, make_response, jsonify
from flask_restful import Resource
import os

app = Flask(__name__)


@app.route('/')
def get_instance():
    return make_response(jsonify({"message": os.environ.get('VM_ID')}))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
