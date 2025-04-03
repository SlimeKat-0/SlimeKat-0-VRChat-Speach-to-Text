from console import Console
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    """Run the console."""
    import sys

    app = QApplication(sys.argv)
    console = Console()
    console.show()
    app.exec()