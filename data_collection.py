import pygetwindow as gw
import pyautogui
import time

def get_active_window():
    try:
        window = gw.getActiveWindow()
        return window.title
    except Exception:
        return None

# Test the function
print(get_active_window())

def timestamp_click():
    return time.time()  # returns the current time in seconds since the epoch as a float

# Test the function
print(timestamp_click())