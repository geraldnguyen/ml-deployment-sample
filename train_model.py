import numpy as np
from sklearn.model_selection import train_test_split
import joblib
from RandomModel import RandomModel

# Generate random data
np.random.seed(42)
X = np.random.rand(1000, 10)  # 1000 samples with 10 features (you can adjust as needed)
y = np.random.choice([0, 1], size=(1000,), p=[0.5, 0.5])  # Binary outcome with 50% chance of each class

# Split the data into training and testing sets
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model
# Model that predicts 0 or 1 randomly
model = RandomModel()
model.fit(X_train, y_train)

# Save the trained model to a file using standalone joblib
model_filename = 'random_model.joblib'
joblib.dump(model, model_filename)

print(f"Model trained and saved to {model_filename}")
