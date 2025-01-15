import pyautogui
import time

# Give yourself 5 seconds to switch to the browser window
print("Switch to your browser or scrollable window. Starting in 5 seconds...")
time.sleep(5)

# Test scrolling directly
print("Scrolling down...")
pyautogui.scroll(-10)  # Negative value scrolls down; increase for faster scrolling
time.sleep(2)

print("Scrolling up...")
pyautogui.scroll(10)  # Positive value scrolls up
