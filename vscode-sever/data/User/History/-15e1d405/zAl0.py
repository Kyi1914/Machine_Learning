from flask import Flask, render_template, request
import carpriceprediction

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(request.form['mileage']),
                      float (request.form['year']),
                      float(request.form['brand'])]
    prediction = carpriceprediction.fn_predict(input_features)
    return render_template('index.html',prediction=prediction)

if __name__ == '__main__':
    app.run()