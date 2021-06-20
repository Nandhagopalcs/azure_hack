import numpy as np
from flask import Flask, request, jsonify, render_template,session
import pickle
import os
from werkzeug.utils import secure_filename
import pymongo
from datetime import date


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)