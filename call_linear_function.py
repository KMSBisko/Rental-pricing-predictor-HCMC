# call_regression_function.py

from linear_regression import train_polynomial_regression, load_trained_model, predict_price
import pandas as pd


def main():
    # Replace 'your_data.csv' with the actual path to your CSV file
    file_path = 'Housing_data_final(11).csv'

    # Replace with the features you want to use
    num_vars = ['area', 'bedrooms', 'bathrooms', 'washingmachine',
                'dtcenter', 'kitchen', 'ac', 'balcony', 'parking', 'furnish']

    # Train the model and save it (uncomment the following line if you haven't trained the model yet)
    model, poly = train_polynomial_regression(
        file_path, num_vars, save_model_path='trained_model.pkl')

    # Load the trained model and polynomial features
    model, poly = load_trained_model(
        'trained_model.pkl', 'trained_model_poly.pkl')

    # User input for feature values
    vari = int(0)
    value = [24, 1, 1, 1, 8, 1, 1, 1, 1, 2]
    user_input = {}
    for var in num_vars:
        # value = float(input())
        # user_input[var] = value
        user_input[var] = value[vari]
        vari = vari+1

    # Create a DataFrame for user input
    user_df = pd.DataFrame([user_input])
    # print(user_df)
    # Predict the price for the user input
    predicted_price = predict_price(model, poly, user_df)

    print(predicted_price)


if __name__ == "__main__":
    main()
