import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
df = pd.read_csv('mock_gas_data.csv')

# Split data
X = df[['Gas Level']]   # features
y = df['Status']        # labels

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save model
with open('gas_ai_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as gas_ai_model.pkl")