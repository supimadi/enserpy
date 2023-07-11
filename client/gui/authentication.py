import typing
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import (
    QFormLayout, QGroupBox, QLineEdit, QPushButton, QVBoxLayout, QWidget
)

class Auth(QGroupBox):
    messaage = pyqtSignal(str)

    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setTitle("Autentikasi")

        layout = QVBoxLayout()

        layout.addWidget(self._token_group())

        self.setLayout(layout)

    def _token_group(self) -> QWidget:
        widget = QWidget()
        layout = QFormLayout()

        send_button = QPushButton("Kirim Pesan")
        token_field = QLineEdit()

        layout.addRow("Pesan", token_field)
        layout.addRow(send_button)

        def send_message():
            self.messaage.emit(token_field.text())

        send_button.clicked.connect(send_message)

        widget.setLayout(layout)
        return widget

