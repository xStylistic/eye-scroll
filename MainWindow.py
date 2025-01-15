from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap
import cv2
import threading

class MainWindow(QMainWindow):
    def __init__(self, eye_tracker, scroller):
        super().__init__()
        self.eye_tracker = eye_tracker
        self.scroller = scroller
        self.tracking = False
        self.latest_frame = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Eye-Tracking Auto-Scroller")
        layout = QVBoxLayout()

        # Start Button
        self.start_button = QPushButton("Start Eye Tracking")
        self.start_button.clicked.connect(self.start_tracking)
        layout.addWidget(self.start_button)

        # Stop Button
        self.stop_button = QPushButton("Stop Eye Tracking")
        self.stop_button.clicked.connect(self.stop_tracking)
        layout.addWidget(self.stop_button)

        # Video Feed
        self.video_label = QLabel(self)
        layout.addWidget(self.video_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_tracking(self):
        if not self.tracking:
            self.tracking = True
            threading.Thread(target=self.run_tracking).start()

    def stop_tracking(self):
        self.tracking = False
        self.scroller.stop_scrolling()

    def run_tracking(self):
        cap = cv2.VideoCapture(0)
        while self.tracking:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture video frame.")
                break

            # Process frame for eye tracking
            eyes_open = self.eye_tracker.process_frame(frame)
            print(f"Eyes Open: {eyes_open}")  # Debugging output

            if eyes_open:
                self.scroller.start_scrolling()
            else:
                self.scroller.stop_scrolling()

            self.update_video_feed(frame)

        cap.release()
        cv2.destroyAllWindows()

    def start_tracking(self):
        print("Start tracking button clicked")  # Debugging message
        if not self.tracking:
            self.tracking = True
            threading.Thread(target=self.run_tracking, daemon=True).start()

    def update_video_feed(self, frame):
        # Convert OpenCV frame to QImage for PyQt display
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = rgb_image.shape
        qimg = QImage(rgb_image.data, width, height, width * channel, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qimg))
