import random

from flask import Flask, make_response, jsonify
from flask_restful import Resource
import os

app = Flask(__name__)

vm_id = None


def gen_uid():
    return str(random.randint(1000, 9999))


@app.route('/')
def get_instance():
    global vm_id
    if vm_id is None:
        vm_id = gen_uid()
    # vm_id = gen_uid()
    return make_response(jsonify({"message": vm_id}))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
