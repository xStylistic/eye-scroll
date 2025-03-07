import sys
from PyQt5.QtWidgets import QApplication

from EyeTracker import EyeTracker
from MainWindow import MainWindow
from Scroller import Scroller


if __name__ == "__main__":
    app = QApplication(sys.argv)

    eye_tracker = EyeTracker()
    scroller = Scroller()
    main_window = MainWindow(eye_tracker, scroller)
    main_window.show()

    sys.exit(app.exec_())
