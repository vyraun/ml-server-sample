from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Please use: http://127.0.0.1:8863/predict?query="

@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query = request.args.get('query') # have to clean the request json
     prediction = [ query, " we will predict something", "like two-three times" ]  #clf.predict(query)
     return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
     #clf = joblib.load('model.pkl') # Just have to load the saved model: pytorch 
     app.run(port=8863, debug=True)
