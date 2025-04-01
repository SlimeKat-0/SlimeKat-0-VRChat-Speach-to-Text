# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect the Exit button to close the application
        self.ui.pushButton_2.clicked.connect(QApplication.instance().quit)

        # Connect the Connect button to retrieve IP and port
        self.ui.connect.clicked.connect(self.retrieve_ip_port)

    def retrieve_ip_port(self):
        # Retrieve the IP and port from the UI
        ip = self.ui.ip.text()
        port = self.ui.port.text()

        # Set them as variables
        print(f"IP: {ip}, Port: {port}")  # For debugging purposes
        self.ip = ip
        self.port = port

        # Close the UI window
        self.close()

def main():
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

# Run the application only if the script is executed directly
if __name__ == "__main__":
    main()