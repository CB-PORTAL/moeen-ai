# Changes to be made: This script needs to load data from all the newly created Workflow Loops.
# All the newly created workflow loops created through learning mode needs to have a data preprocessing feature.
# Need to give the machine learning model the right data translation so that it can normalize and read the data.

# This script loads the data from the `m_clicks_coordinates.csv` file, normalizes the data, and splits the data into training and testing datasets.

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

scaler = MinMaxScaler()  # Make scaler a global variable to be used by preprocess_click()

def load_data():
    # Load data from CSV file
    data = pd.read_csv('F:\Workspace\MOEEN_AI\env_moeen\m_clicks_coordinates.csv')

    # Check if we have at least 3 mouse clicks
    if len(data) < 3:
        return None, None, None, None  # Not enough data to create sequences

    # Normalize the X and Y coordinates
    data[['X', 'Y']] = scaler.fit_transform(data[['X', 'Y']])

    # Group the data into sequences of 3 clicks
    sequences = data[['X', 'Y']].rolling(window=3, min_periods=3).apply(list)

    # Split the data into features (X) and target (y)
    X = np.array([seq for seq in sequences.values if seq is not None])[:-1]
    y = np.array([seq for seq in sequences.shift(-1).values if seq is not None])[:-1]

    # Reshape X to be [samples, time steps, features]
    X = X.reshape((X.shape[0], 1, X.shape[1], 2))  # 2 features: X and Y coordinates

    # Split the data into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, y_train, X_test, y_test

def preprocess_click(click):
    # Scale the X and Y coordinates between 0 and 1
    scaled_click = scaler.transform([click])

    return scaled_click.reshape((1, 2, 1))  # Reshape to be [samples, time steps, features]
