# call_regression_function.py

from linear_reg import train_polynomial_regression, predict_price
import pandas as pd


def main():
    # Replace 'your_data.csv' with the actual path to your CSV file
    file_path = 'D:\mtrie\OneDrive\Documents\IT\python\hs3\Housing_data_final(2).csv'

    # Replace with the features you want to use
    num_vars = ['area', 'bedrooms', 'bathrooms', 'washingmachine', 'dtcenter',
                'dtrec', 'dthospital', 'hotwater', 'ac', 'furnish', 'parking', 'security']

    # Train the model
    model, poly = train_polynomial_regression(file_path, num_vars)
    
    # User input for feature values
    vari = int(0)
    value = [100, 1, 1, 1, 0.1, 0.2, 0.3, 1, 1, 1, 1, 1]

    user_input = {}
    for var in num_vars:
        # value = float(input(f"Enter the value for {var}: "))
        user_input[var] = value[vari]
        vari = vari+1

    # Create a DataFrame for user input
    user_df = pd.DataFrame([user_input])
    # Predict the price for the user input
    predicted_price = predict_price(model, poly, user_df)

    print(f'Predicted Price: {predicted_price}')


if __name__ == "__main__":
    main()
