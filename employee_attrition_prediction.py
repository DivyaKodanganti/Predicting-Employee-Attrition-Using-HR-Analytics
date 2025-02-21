# -*- coding: utf-8 -*-
"""Employee Attrition Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11NYVv97Lb-q_Pq9dyLowTZad-qIYMzjs
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import GridSearchCV

from google.colab import files
uploaded = files.upload()

# Load dataset after upload
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Display the first few rows of the dataset
df.head()

# First, let's check which columns are categorical and numeric
print(df.dtypes)

# You can either drop non-numeric columns or convert them to numeric.
# Let's drop non-numeric columns first (if any).
numeric_df = df.select_dtypes(include=[np.number])

# Now compute the correlation matrix for the numeric columns only
corr = numeric_df.corr()

# Heatmap to check correlations between numeric features
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Drop irrelevant columns
df = df.drop(['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'], axis=1)

# One-hot encode categorical variables
df = pd.get_dummies(df, drop_first=True)

# Normalize the data (for better performance in many models)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.drop('Attrition_Yes', axis=1))

# Add the scaled features back to the dataframe
df_scaled = pd.DataFrame(scaled_features, columns=df.drop('Attrition_Yes', axis=1).columns)
df_scaled['Attrition_Yes'] = df['Attrition_Yes']
df_scaled.head()

# Split data into features and target variable
X = df_scaled.drop('Attrition_Yes', axis=1)
y = df_scaled['Attrition_Yes']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check the shape of the splits
print(f"Train Set: {X_train.shape}, Test Set: {X_test.shape}")

# Initialize the Random Forest model
rf_model = RandomForestClassifier(random_state=42)

# Hyperparameter tuning using GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Best parameters
print(f"Best Parameters: {grid_search.best_params_}")

# Best model
best_rf_model = grid_search.best_estimator_

# Predictions on the test set
y_pred = best_rf_model.predict(X_test)

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# ROC-AUC Score
roc_auc = roc_auc_score(y_test, y_pred)
print(f"ROC-AUC Score: {roc_auc}")

# Get feature importance from the model
feature_importance = best_rf_model.feature_importances_

# Create a DataFrame to visualize feature importance
features = X.columns
importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': feature_importance
})

# Sort by importance
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Visualize the feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df)
plt.title('Feature Importance')
plt.show()

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

# Define the model
model = RandomForestClassifier()

# Apply RFE to select important features
rfe = RFE(model, n_features_to_select=10)  # Select top 10 features
X_rfe = rfe.fit_transform(X_train, y_train)

# Show the selected features
selected_features = X_train.columns[rfe.support_]
print("Selected features:", selected_features)

from sklearn.linear_model import LassoCV
import numpy as np

# Lasso regularization for feature selection
lasso = LassoCV()
lasso.fit(X_train, y_train)

# Get the coefficients and select features with non-zero coefficients
selected_features_lasso = X_train.columns[np.where(lasso.coef_ != 0)]
print("Selected features from Lasso:", selected_features_lasso)

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Standardize the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)

# Apply PCA
pca = PCA(n_components=2)  # Reduce to 2 dimensions for visualization
X_pca = pca.fit_transform(X_scaled)

# Visualizing the first two principal components
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_train, cmap='viridis')
plt.title("PCA Visualization")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

# Variance explained by each component
print("Explained variance ratio by each component:", pca.explained_variance_ratio_)

# Define and train the model
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

# Train the model on the training data
model.fit(X_train, y_train)

# Predict probabilities for the positive class (attrition)
y_probs = model.predict_proba(X_test)[:, 1]

# Compute Precision and Recall
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, thresholds = precision_recall_curve(y_test, y_probs)

# Plot Precision-Recall curve
plt.plot(recall, precision, color='b', label='Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.show()

from sklearn.metrics import f1_score

# Predict the classes
y_pred = model.predict(X_test)

# Calculate F1-Score
f1 = f1_score(y_test, y_pred)
print(f"F1-Score: {f1}")