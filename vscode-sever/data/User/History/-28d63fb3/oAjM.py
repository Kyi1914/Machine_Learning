import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import joblib  # For loading the trained model

# Load the trained machine learning model
model = joblib.load('sourceCode/lab1_CarPricePrediction.model')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Machine Learning Prediction App: Car Price Prediction"),
    
    dcc.Input(id='input-features', type='text', placeholder='Enter features...'),
    
    html.Div(id='output-prediction'),
])

@app.callback(
    Output('output-prediction', 'children'),
    [Input('input-features', 'value')]
)
def update_prediction(input_features):
    if input_features:
        # Assuming input features are comma-separated
        input_features = [float(x) for x in input_features.split(',')]

        # Make a prediction using the loaded model
        prediction = model.predict([input_features])[0]
        
        return f"Predicted Value: {prediction:.2f}"
    else:
        return "Enter input features to get a prediction"

if __name__ == '__main__':
    app.run_server(debug=True)
