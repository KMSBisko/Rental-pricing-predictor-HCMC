# polynomial_regression.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import joblib


def train_polynomial_regression(file_path, num_vars, poly_degree=1, save_model_path=None):
    # Load data from CSV file
    data = pd.read_csv(file_path)

    #input data processing for price
    Q1 = data.price.quantile(0.20)
    Q3 = data.price.quantile(0.80)
    IQR = Q3 - Q1
    data = data[(data.price >= Q1 - 1.5*IQR) & (data.price <= Q3 + 1.5*IQR)]

    #input data processing for dtcenter
    Q1 = data.dtcenter.quantile(0.2)
    Q3 = data.dtcenter.quantile(0.80)
    IQR = Q3 - Q1
    data = data[(data.dtcenter >= Q1 - 1.5*IQR) & (data.dtcenter <= Q3 + 1.5*IQR)]

    #input data processing for area
    Q1 = data.area.quantile(0.2)
    Q3 = data.area.quantile(0.80)
    IQR = Q3 - Q1
    data = data[(data.area >= Q1 - 1.5*IQR) & (data.area <= Q3 + 1.5*IQR)]

    # Define the features (independent variables) and target (dependent variable)
    X = data[num_vars]
    y = data['price']

    # Polynomial regression
    poly = PolynomialFeatures(degree=poly_degree)
    X_poly = poly.fit_transform(X)

    # Train the polynomial linear regression model
    model = LinearRegression()
    model.fit(X_poly, y)

    # Save the trained model to a file if a save path is provided
    if save_model_path:
        joblib.dump(model, save_model_path)
        joblib.dump(poly, save_model_path.replace('.pkl', '_poly.pkl'))

    return model, poly


def load_trained_model(model_path, poly_path):
    # Load the trained model and polynomial features
    model = joblib.load(model_path)
    poly = joblib.load(poly_path)

    return model, poly


def predict_price(model, poly, user_input):
    # Transform user input using polynomial features
    user_input_poly = poly.transform(user_input)

    # Predict the price for the user input
    predicted_price = model.predict(user_input_poly)[0]

    return predicted_price
