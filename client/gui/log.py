import typing

from PyQt5.QtWidgets import (
    QFormLayout, QGroupBox, QTextEdit,
    QVBoxLayout, QWidget, QWidget
)

class LogUI(QGroupBox):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setTitle("Log Aplikasi")

        layout = QVBoxLayout()

        layout.addWidget(self._token_group())

        self.setLayout(layout)

    def _token_group(self) -> QWidget:
        widget = QWidget()
        layout = QFormLayout()

        self.log_text = QTextEdit()
        layout.addRow(self.log_text)

        widget.setLayout(layout)
        return widget

    def append_log(self, text) -> None:
        self.log_text.append(str(text))
