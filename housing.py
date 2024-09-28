import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load data from CSV file
file_path = 'D:\mtrie\OneDrive\Documents\IT\python\hs3\Housing_data_final.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Define the features (independent variables) and target (dependent variable)
num_vars = ['area', 'bedrooms', 'bathrooms', 'washingmachine', 'dtcenter', 'dtrec', 'dthospital', 'hotwater', 'ac', 'furnish', 'parking', 'security']
X = data[num_vars]
y = data['price']

# Polynomial regression with degree 2 (you can change the degree as needed)
poly_degree = 2
poly = PolynomialFeatures(degree=poly_degree)
X_poly = poly.fit_transform(X)

# Train the polynomial linear regression model
model = LinearRegression()
model.fit(X_poly, y)

# User input for feature values
user_input = {}
for var in num_vars:
    value = float(input(f"Enter the value for {var}: "))
    user_input[var] = value

# Create a DataFrame for user input
user_df = pd.DataFrame([user_input])

# Transform user input using polynomial features
user_input_poly = poly.transform(user_df)

# Predict the price for the user input
predicted_price = model.predict(user_input_poly)[0]
print(f'Predicted Price: {predicted_price}')