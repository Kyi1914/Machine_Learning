import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import joblib  # For loading the trained model

# Load the trained machine learning model
model = joblib.load('sourceCode/CarPricePrediction.model')
model = pickle_modle['model']
    scaler = pickle_modle['scaler']
    sample = scaler.transform(sample)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Machine Learning Prediction App"),
    
    html.Label("Engine Size:"),
    dcc.Input(id='input-engine', type='number', value=1500),
    
    html.Label("Year:"),
    dcc.Input(id='input-year', type='number', value=2020),
    
    html.Button('Submit', id='submit-button', n_clicks=0),
    
    html.Div(id='output-prediction'),
])

@app.callback(
    Output('output-prediction', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.State('input-engine', 'value'),
     dash.State('input-year', 'value')]
)
def update_prediction(n_clicks, engine_size, year):
    if n_clicks > 0:
        # Make a prediction using the loaded model
        prediction = model.predict([[engine_size, year]])[0]
        
        return f"Predicted Value: {prediction:.2f}"
    else:
        return "Enter engine size and year, then click Submit"

if __name__ == '__main__':
    app.run_server(debug=True)
