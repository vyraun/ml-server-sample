from flask import Flask, jsonify
from flask import request
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/predict', methods=['GET'])
def predict():
     json_ = request.json
     query = "a string after parsing json" # have to clean the request json
     prediction = [" we will predict something", "like two-three times" ]  #clf.predict(query)
     return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
     #clf = joblib.load('model.pkl') # Just have to load the saved model: pytorch 
     app.run(port=8863, debug=True)
