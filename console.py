from PySide6.QtWidgets import QApplication, QDialog
from console_ui import Ui_Console
from multiprocessing import Pipe
import os

class Console(QDialog):
    def send_termination_signal(self):
        import sys
        """Send a termination signal through the pipe and close the application."""
        self.pipe.send("TERMINATE")  # Send a termination signal
        sys.exit()  # Close the Console application

    def __init__(self, pipe, parent=None):
        super().__init__(parent)
        import sys
        self.pipe = pipe
        self.ui = Ui_Console()
        self.ui.setupUi(self)

        # Connect the Close button to exit the application
        self.ui.Close.rejected.connect(self.send_termination_signal)

    def send_termination_signal(self):
        import sys
        """Send a termination signal through the pipe and close the application."""
        self.pipe.send("TERMINATE")  # Send a termination signal
        os._exit(0)


    def update_console_text(self, text2):
        """Update the console text label."""
        self.ui.Console_2.setText(text2)

def start_con(pipe):
    """Run the console and receive data from the pipe."""
    import sys

    app = QApplication(sys.argv)
    console = Console(pipe)
    console.show()

    # Continuously listen for data from the pipe
    def listen_for_updates():
        while True:
            if pipe.poll():  # Check if there is data in the pipe
                text2 = pipe.recv()  # Receive the text from the pipe
                console.update_console_text(text2)

    # Start listening for updates in a separate thread
    from threading import Thread
    listener_thread = Thread(target=listen_for_updates, daemon=True)
    listener_thread.start()

    sys.exit(app.exec())

if __name__ == "__main__":
    print("This script is intended to be run as a subprocess.")