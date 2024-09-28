# polynomial_regression.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def train_polynomial_regression(file_path, num_vars, poly_degree=2):
    # Load data from CSV file
    data = pd.read_csv(file_path)

    # Define the features (independent variables) and target (dependent variable)
    X = data[num_vars]
    y = data['price']

    # Polynomial regression
    poly = PolynomialFeatures(degree=poly_degree)
    X_poly = poly.fit_transform(X)

    # Train the polynomial linear regression model
    model = LinearRegression()
    model.fit(X_poly, y)

    return model, poly

def predict_price(model, poly, user_input):
    # Transform user input using polynomial features
    user_input_poly = poly.transform(user_input)

    # Predict the price for the user input
    predicted_price = model.predict(user_input_poly)[0]

    return predicted_price
