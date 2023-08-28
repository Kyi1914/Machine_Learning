import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import matplotlib
import pickle

filename = 'sourceCode/CarPricePrediction.model'
print("loaded file")

def fn_predict(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,2)
    # loaded_model = pickle.load(open(filename, 'rb'))
    
    result = loaded_model.predict(to_predict)
    return np.exp(result[0])
    # return result[0]
    
print("*****  successfully called car price prediction  *****")