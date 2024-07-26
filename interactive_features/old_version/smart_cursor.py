import tkinter as tk
import pyautogui
import time

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()

def automate_mouse():
    # Define the coordinates for the three points of the triangle.
    points = [(500, 500), (screenWidth / 2, screenHeight / 2), (500, screenHeight / 2)]

    # Repeat the movement indefinitely.
    while True:
        for point in points:
            # Move the mouse to the current point.
            pyautogui.moveTo(point[0], point[1], duration=1)  # Add a duration for the move.
            time.sleep(3)  # Pause for 3 seconds.
            # Click the mouse.
            pyautogui.click()
            time.sleep(3)  # Pause for 3 seconds.

root = tk.Tk()

button = tk.Button(root, text='Automate Mouse', command=automate_mouse)
button.pack()

# Replace 'path-to-your-cursor-file.cur' with the path to your actual cursor file.
root.config(cursor='@F:/Workspace/MOEEN_AI/Assets/Cursors/v1/DefaultCursor_v1.cur')

root.mainloop()
