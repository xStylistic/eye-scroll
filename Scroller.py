import pyautogui
import time

import threading

class Scroller:
    def __init__(self, scroll_amount=10, reverse=False):
        """
        @param scroll_amount: Amount to scroll per iteration.
        @param reverse: Set True if your OS reverses the scrolling direction.
        """
        self.is_scrolling = False
        self.scroll_thread = None
        self.direction = "none"  # "up", "down", or "none"
        self.scroll_amount = scroll_amount
        self.reverse = reverse

    def start_scrolling(self, direction):
        # Always update the direction.
        self.direction = direction
        print(f"start_scrolling called with direction: {direction}")
        if not self.is_scrolling:
            print("Starting scrolling...")
            self.is_scrolling = True
            self.scroll_thread = threading.Thread(target=self.scroll, daemon=True)
            self.scroll_thread.start()

    def scroll(self):
        while self.is_scrolling:
            print(f"Scrolling... Current direction: {self.direction}")
            if self.direction == "up":
                # For "up" gaze, scroll up.
                amount = self.scroll_amount if not self.reverse else -self.scroll_amount
                print(f"Detected gaze: up --> Scrolling up with amount: {amount}")
                pyautogui.scroll(amount)
            elif self.direction == "down":
                # For "down" gaze, scroll down.
                amount = -self.scroll_amount if not self.reverse else self.scroll_amount
                print(f"Detected gaze: down --> Scrolling down with amount: {amount}")
                pyautogui.scroll(amount)
            time.sleep(0.1)

    def stop_scrolling(self):
        print("Stopping scrolling...")
        self.is_scrolling = False
        self.direction = "none"
