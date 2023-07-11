import typing

from PyQt5 import QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import (
    QGridLayout, QMainWindow, QWidget
)

from .authentication import Auth
from .server import ServerUI
from .log import LogUI


class MainWindow(QMainWindow):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Inspeksi Muatan Gerbong KAI")

        widget = QWidget()
        layout = QGridLayout()

        self.auth = Auth(self)
        self.server_ui = ServerUI(self)
        self.log_ui = LogUI(self)

        self.auth.messaage.connect(self.server_ui.send_message)
        self.server_ui.server_msg.connect(self.log_ui.append_log)

        layout.addWidget(self.auth, 0, 0, 2, 1)
        layout.addWidget(self.server_ui, 0, 1)
        layout.addWidget(self.log_ui, 1, 1)

        self.server_ui.server_started.connect(self._start_load_cell)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def _start_load_cell(self):
        pass

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.server_ui.stop_server()
        return super().closeEvent(a0)
