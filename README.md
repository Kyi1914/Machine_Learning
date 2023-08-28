# Machine_Learning

## Brief Introduction about this project

In this repository, I developed a model to predict car prices for the Chaky Company. The dataset I utilized was the 'Cars.csv' dataset. I performed various data preparation steps such as data cleaning and label encoding, among others. You can find detailed information about the steps I took in my Jupyter notebook, which I highly recommend reading.

## Quick start

To explore this project, you'll need Docker or a compiler that can interpret Jupyter notebooks, along with an IDE like VScode. I conducted three rounds of experiments, selecting different pairs of features for each round. If you're interested in checking the best version of my experiments, please refer to "CarPricePrediction.ipynb" directly.

Here are the acknowledgements for the three notebooks:
- First experiment: "CarPricePrediction2f_v1.0.ipynb"
- Second experiment: "CarPricePrediction2f_v2.0.ipynb"
- Third experiment (best version): "CarPricePrediction.ipynb"

Based on my experiments, the third version can be considered the best as it achieved the smallest mean squared error (mse).

I also deployed my model to allow easy access and testing. If you want to access a web version and perform testing with your own data, you can do so through "app_flask.py".

### About Deployment and Flask:
For deployment, I created "app_flask.py" to mediate between my model and the HTML page. I designed the HTML layout in "index.html," which is located in the templates folder. Additionally, I developed a separate file named "carpriceprediction.py" to work with my model.

## Conclusion:
I summarized the outcomes of these experiments at the end of the third Jupyter notebook.

Thank you for your interest in my project.