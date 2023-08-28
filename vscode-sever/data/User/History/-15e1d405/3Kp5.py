from flask import Flask, render_template, request
import carprice_prediction

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(request.form['max_power']),
                      float(request.form['car_age']),
                      float(request.form['mileage'])]
    prediction = predict_car_price.fn_predict(input_features)
    return render_template('index.html',prediction=prediction)

if __name__ == '__main__':
    app.run()