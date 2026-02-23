import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import pickle
import os

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/sales_data.csv")

X = df[["Marketing_Spend", "Employees", "Time"]]
y = df["Sales"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"R2 Score: {r2}")
print(f"MSE: {mse}")

# Save model
model_path = os.path.join("models", "model.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✅ Model Trained & Saved at:", model_path)