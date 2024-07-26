import os
import sys
import time
from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener, Key
from tkinter import Tk, Canvas
from PIL import Image, ImageTk

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import pyautogui
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import Adam

import data_collection
import data_loading

print(pyautogui.__file__)
print("Current working directory:", os.getcwd())

class WorkflowLoop:
    def __init__(self):
        self.learning_mode = False
        self.training_mode = False
        self.current_file = None
        self.df = None

    def ask_mode(self):
        self.learning_mode = input("Do you want to turn on Learning Mode? (Y/N): ").lower() == 'y'
        if self.learning_mode:
            self.start_learning_mode()
        else:
            self.training_mode = input("Do you want to turn on Training Mode? (Y/N): ").lower() == 'y'

    def start_learning_mode(self):
        self.current_file = input("Please enter the name of the new csv file for this session: ")
        self.df = pd.DataFrame(columns=['X', 'Y'])

    def stop_learning_mode(self):
        if self.df is not None and self.current_file is not None:
            self.df.to_csv(self.current_file, index=False)
        self.learning_mode = False
        self.current_file = None
        self.df = None

    def record_click(self, x, y):
        if self.learning_mode:
            new_data = {'X': x, 'Y': y}
            self.df = self.df.append(new_data, ignore_index=True)

    def edit_loop(self):
        csv_file_name = input("Please enter the name of the csv file you want to edit: ")
        if os.path.exists(csv_file_name):
            self.df = pd.read_csv(csv_file_name)
            self.current_file = csv_file_name
            self.start_learning_mode()
        else:
            print(f"No such file: {csv_file_name}")

workflow = WorkflowLoop()
workflow.ask_mode()

def create_model(n_steps, n_features):
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
    model.add(Dense(2))
    model.compile(optimizer=Adam(), loss='mse')
    return model

def load_data():
    # Check if the CSV file exists.
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"The CSV file {csv_path} does not exist.")

    # Read the CSV file into a Pandas DataFrame.
    data = pd.read_csv(csv_path)

    # Check if the DataFrame has the `X` and `Y` columns.
    if not ('X' in data.columns and 'Y' in data.columns):
        raise ValueError(f"The CSV file {csv_path} does not have the `X` and `Y` columns.")

    # Convert the `X` and `Y` columns to floats.
    data['X'] = data['X'].astype(float)
    data['Y'] = data['Y'].astype(float)

    # Split the DataFrame into training and test sets.
    X_train, X_test, y_train, y_test = train_test_split(data[['X', 'Y']], data[['Label']], test_size=0.2, random_state=42)

    return X_train, y_train, X_test, y_test

def preprocess_click(click):
    screen_width, screen_height = pyautogui.size()
    normalized_click = [click[0] / screen_width, click[1] / screen_height]
    return np.array(normalized_click).reshape(1, 1, -1)

def simulate_click(x, y):
    screen_width, screen_height = pyautogui.size()
    scaled_x = x * screen_width
    scaled_y = y * screen_height
    pyautogui.moveTo(scaled_x, scaled_y)
    pyautogui.click()

def on_click(x, y, button, pressed):  
    global df
    global model
    global learning_mode
    global training_mode  

    # Change the cursor to the custom image on mouse press
    if pressed:
        canvas.config(cursor="@venv/Assets/v1/your_cursor.cur")

    # Only proceed if the click is within the bounds of a 1920x1080 screen
    if 0 <= x <= 1920 and 0 <= y <= 1080:  
        if learning_mode and pressed:  
            df.loc[len(df)] = [x, y]
            df.to_csv('m_clicks_coordinates.csv', index=False)
            if time.time() % 300 < 1:
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                df.to_csv(f'm_clicks_coordinates_backup_{timestamp}.csv', index=False)

        if training_mode:
            X_train, y_train, X_test, y_test = load_data()  
            if X_train is not None:  
                print("Training the model...")
                n_steps, n_features = 1, 2
                model = create_model(n_steps, n_features)
                model.fit(np.array(X_train).reshape(-1, 1, 2), y_train, epochs=200, verbose=0)

            if model is not None:  
                new_click = preprocess_click([x, y])
                prediction = model.predict(new_click)
                print(f'Prediction: {prediction}')

    # Reset the cursor to the default image when the mouse button is released
    else:
        canvas.config(cursor="")

def on_press(key):
    global learning_mode
    # Change the cursor to the custom image on key press
    canvas.config(cursor="@venv/Assets/v1/your_cursor.cur")

    if key == Key.ctrl and key.char == 'm':
        learning_mode = not learning_mode
        print(f"Learning mode is now {'on' if learning_mode else 'off'}")

def train_model(csv_file_name):
    data = pd.read_csv(csv_file_name)
    model = RandomForestClassifier()
    model.fit(data[["X", "Y"]], data["Label"])
    joblib.dump(model, "./model.pkl")

def main():
    print("Do you want to turn on Learning Mode?")
    choice = input("(Y/N): ")

    if choice.lower() == "y":
        print("Learning Mode is turned on.")
        # Call your load_data function here

        X_train, y_train, X_test, y_test = load_data()

        if X_train is not None:
            print("Training the model...")
            n_steps, n_features = 1, 2
            model = create_model(n_steps, n_features)
            model.fit(np.array(X_train).reshape(-1, 1, 2), y_train, epochs=200, verbose=0)
   
        with Listener(on_click=on_click) as listener, KeyboardListener(on_press=on_press) as key_listener:
            listener.join()
            key_listener.join()

    elif choice.lower() == "n":
        print("Do you want to turn on Training Mode instead?")
        choice = input("(Y/N): ")

        if choice.lower() == "y":
            print("The following csv files are available for training the model:")
            for csv_file in os.listdir("./data"):
                print(csv_file)

            print("Please choose a csv file to train the model: ")
            csv_file_name = input()

            train_model(csv_file_name)

    else:
        print("Exiting...")
        sys.exit()

if __name__ == "__main__":
    main()
