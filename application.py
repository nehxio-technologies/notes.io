import sys
from PySide6.QtWidgets import QApplication


class Notes(QApplication):
    def __init__(self):
        super(Notes, self).__init__([])

    def run(self):
        sys.exit(self.exec())
