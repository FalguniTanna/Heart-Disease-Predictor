import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv('heart.csv')

# Check for missing values and drop rows with missing values
df.dropna(inplace=True)

# Convert categorical columns using one-hot encoding
df = pd.get_dummies(df, columns=['cp', 'restecg', 'slope', 'thal', 'sex', 'exang', 'dataset'], drop_first=True)

# Normalize numerical columns
numerical_features = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak']
scaler = StandardScaler()
df[numerical_features] = scaler.fit_transform(df[numerical_features])
# Example mapping (if applicable)
df['num'] = df['num'].replace({2: 1, 3: 1, 4: 1})  # Replace other classes with 1 for Heart Disease

# Split data into features (X) and target (y)
X = df.drop('num', axis=1)  # Ensure 'num' is the target column
y = df['num']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model, scaler, and columns
joblib.dump(model, 'heartdiseasemodel.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(X.columns, 'columns.pkl')

print("Model training complete and files saved.")
print(df['num'].unique()) 
