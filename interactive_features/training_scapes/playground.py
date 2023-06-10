from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class SmartCursor(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

        # Load your cursor design
        self.setPixmap(QtGui.QPixmap('F:\\Workspace\\MOEEN_AI\\Assets\\Cursors\\v1\\DefaultCursor_v1.png'))

        # Set the widget to be transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Make the widget frameless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # Start the timer to update the position every 10 ms
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_position)
        self.timer.start(10)

    def update_position(self):
        # Get the global position of the system cursor
        global_pos = QtGui.QCursor.pos()

        # Move the smart cursor to the position of the system cursor
        self.move(global_pos)

    def mousePressEvent(self, event):
        event.ignore()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window to be transparent
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowSystemMenuHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Create a container widget with a border
        container = QtWidgets.QWidget(self)
        container.setFocusPolicy(QtCore.Qt.StrongFocus)  # Set focus policy
        container.setStyleSheet("border: 10px solid black;")
        container_layout = QtWidgets.QVBoxLayout(container)

        # Set the WA_TransparentForMouseEvents attribute
        container.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        # Add the Smart Cursor
        self.smart_cursor = SmartCursor()
        container_layout.addWidget(self.smart_cursor)

        # Set the central widget of the MainWindow to the container
        self.setCentralWidget(container)

        # Set the default window size
        self.setGeometry(100, 100, 800, 600)

        # Show the window at its current size and position
        self.show()

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.exec_())