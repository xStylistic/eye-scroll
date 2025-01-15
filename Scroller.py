import pyautogui
import time

import threading

class Scroller:
    def __init__(self):
        self.is_scrolling = False
        self.scroll_thread = None

    def start_scrolling(self):
        if not self.is_scrolling:
            print("Starting scrolling...")  # Debugging message
            self.is_scrolling = True
            self.scroll_thread = threading.Thread(target=self.scroll, daemon=True)
            self.scroll_thread.start()

    def scroll(self):
        while self.is_scrolling:
            print("Scrolling...")  # Debugging message
            pyautogui.scroll(-10)  # Adjust as needed
            time.sleep(0.1)

    def stop_scrolling(self):
        if self.is_scrolling:
            print("Stopping scrolling...")  # Debugging message
        self.is_scrolling = False
