import typing
import socket

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import (
    QFormLayout, QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QVBoxLayout, QWidget, QWidget
)

class ServerUI(QGroupBox):
    messaage = pyqtSignal(str)
    server_msg = pyqtSignal(str)

    server_started = pyqtSignal()
    server_stopped = pyqtSignal()

    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setTitle("Server")

        self.server = None
        #  self.server_thread = QThread()

        #  self.server.moveToThread(self.server_thread)
        #  self.server_thread.started.connect(self.server.start_server)
        #  self.server.finished.connect(self.server_thread.quit)

        layout = QVBoxLayout()
        layout.addWidget(self._token_group())

        self.setLayout(layout)

    def send_message(self, msg: str):
        if not self.server:
            return

        self.server.sendall(msg.encode()) # kirim pesan ke server (harus byte)
        self.server_msg.emit(self.server.recv(1024).decode("UTF-8")) # baca pesan yang diberikan server

    def _start_server(self) -> None:
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # membuat socket
            self.server.connect(("127.0.0.1", 6969)) # connect ke alamat ip dan port server
        except Exception as es:
            print("Error: Gagal Konek ke server")
            return

        #  self.server.finished.connect(self.server.deleteLater)
        #  self.server_thread.finished.connect(self.server_thread.deleteLater)

        #  self.server_thread.start()

        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

        self.status.setText("STARTED")
        self.status.setStyleSheet(
            """
            QLabel {
                color: green;
                border: 1px solid green;
                padding: 10px;
                border-radius: 5px;
            }
            """
        )

        self.server_started.emit()

    def stop_server(self):
        if self.server:
            self.server.close()

        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

        self.status.setText("STOPPED")
        self.status.setStyleSheet(
            """
            QLabel {
                color: red;
                border: 1px solid red;
                padding: 10px;
                border-radius: 5px;
            }
            """
        )

        self.server_stopped.emit()

    def _token_group(self) -> QWidget:
        widget = QWidget()

        layout = QFormLayout()
        layout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        layout.setFormAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout.setLabelAlignment(Qt.AlignLeft)

        self.status = QLabel("STOPPED")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet(
            """
            QLabel {
                color: red;
                border: 1px solid red;
                padding: 10px;
                border-radius: 5px;
            }
            """
        )

        self.start_btn = QPushButton("Start Server")
        self.stop_btn = QPushButton("Stop Server")
        self.stop_btn.setEnabled(False)

        self.start_btn.clicked.connect(self._start_server)
        self.stop_btn.clicked.connect(self.stop_server)

        def button_group() -> QWidget:
            w = QWidget()
            l = QHBoxLayout()

            l.addWidget(self.start_btn)
            l.addWidget(self.stop_btn)

            w.setLayout(l)
            return w

        layout.addRow("Server Status", self.status)
        layout.addRow(button_group())

        widget.setLayout(layout)
        return widget
