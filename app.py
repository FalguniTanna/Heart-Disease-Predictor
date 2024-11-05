# # Flask Application

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import joblib
# import pandas as pd

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)

# # Load the model, scaler, and columns
# model = joblib.load('heartdiseasemodel.pkl')
# scaler = joblib.load('scaler.pkl')
# columns = joblib.load('columns.pkl')

# # Function to preprocess input data
# def preprocess_input(data):
#     # Convert the input data into a DataFrame
#     input_df = pd.DataFrame([data], columns=X.columns)  # Use X's columns for structure
    
#     # Apply one-hot encoding
#     input_df = pd.get_dummies(input_df, columns=['cp', 'restecg', 'slope', 'thal'], drop_first=True)
    
#     # Reindex the columns to match the training set
#     input_df = input_df.reindex(columns=columns, fill_value=0)
    
#     # Scale the numerical features
#     input_df = scaler.transform(input_df)
    
#     return input_df

# # Define the prediction route
# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Extract the input data from the request
#         data = request.json['data']
        
#         # Preprocess the input data
#         processed_data = preprocess_input(data)
        
#         # Make the prediction using the trained model
#         prediction = model.predict(processed_data)
        
#         # Return the prediction result
#         return jsonify({'prediction': int(prediction[0])})
    
#     except Exception as e:
#         return jsonify({'error': str(e)})

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load the model, scaler, and columns
model = joblib.load('heartdiseasemodel.pkl')
scaler = joblib.load('scaler.pkl')
columns = joblib.load('columns.pkl')

# Define the numerical features that need scaling
numerical_features = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak']

# Function to preprocess input data
def preprocess_input(data):
    # Convert the input data into a DataFrame
    input_df = pd.DataFrame([data], columns=[
        'age', 'sex', 'dataset', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
        'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
    ])
    
    # Apply one-hot encoding
    input_df = pd.get_dummies(input_df, columns=['cp', 'restecg', 'slope', 'thal', 'sex', 'exang'], drop_first=True)

    # Print columns after encoding
    print(f"Columns after encoding: {input_df.columns.tolist()}")
    
    # Reindex the columns to match the training set
    input_df = input_df.reindex(columns=columns, fill_value=0)
    
    # Print columns after reindexing
    print(f"Columns after reindexing: {input_df.columns.tolist()}")
    
    # Scale the numerical features
    input_df[numerical_features] = scaler.transform(input_df[numerical_features])
    
    return input_df

# def preprocess_input(data):
#     # Convert the input data into a DataFrame
#     input_df = pd.DataFrame([data], columns=[
#         'age', 'sex', 'dataset', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
#         'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
#     ])
    
#     # Apply one-hot encoding (the same way it was done during training)
#     input_df = pd.get_dummies(input_df, columns=['cp', 'restecg', 'slope', 'thal', 'sex', 'exang'], drop_first=True)
    
#     # Reindex the columns to match the training set (fill missing columns with 0)
#     input_df = input_df.reindex(columns=columns, fill_value=0)
    
#     # Scale the numerical features
#     input_df[numerical_features] = scaler.transform(input_df[numerical_features])
    
#     return input_df

#     # Convert the input data into a DataFrame
#     # input_df = pd.DataFrame([data], columns=columns)
    
#     # # Scale the numerical features
#     # input_df[numerical_features] = scaler.transform(input_df[numerical_features])
    
#     # return input_df

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract the input data from the request
        data = request.json['data']
        
        # Preprocess the input data
        processed_data = preprocess_input(data)
        
        # Make the prediction using the trained model
        prediction = model.predict(processed_data)
        
        # Print the raw prediction for debugging
        print(f"Raw Prediction: {prediction}")  # This should show the actual predicted value
        
        # Map the prediction to "Heart Disease" or "Not Heart Disease"
        if prediction[0] in [0]:
            result = "Not Heart Disease"
        elif prediction[0] in [1]:
            result = "Heart Disease"
        else :
            result = "Other Disease"


        return jsonify({'prediction': result})
    
    except Exception as e:
        return jsonify({'error': str(e)})




# Run the app
if __name__ == '__main__':
    app.run(debug=True)
