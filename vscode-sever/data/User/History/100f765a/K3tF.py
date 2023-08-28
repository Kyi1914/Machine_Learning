import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import matplotlib
import pickle

modelname = 'sourceCode/CarPricePrediction.model'

def fn_predict(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,3)
    
    #loaded model
    pickle_model = pickle.load(open(filename, 'rb'))
    
    #
    model = pickle_model['model']
    scaler = pickle_model['scaler']
    
    print("loaded model")
    
    to_predict = scaler.transform(to_predict)
    result = model.predict(to_predict)
    return np.exp(result[0])
    # return result[0]
    
print("*****  successfully called car price prediction  *****")