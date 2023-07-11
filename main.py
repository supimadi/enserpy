#  import socket

#  HOST = "172.23.0.1"  # The server's hostname or IP address
#  PORT = 6969  # The port used by the server

#  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#      s.connect((HOST, PORT))
#      s.sendall(b"Hello, world")
#      data = s.recv(1024)

#  print(f"Received {data!r}")

import sys
import os

import qdarktheme

from PyQt5.QtWidgets import QApplication

from client import MainWindow


def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

    app = QApplication([])

    ex = MainWindow()
    ex.setMinimumSize(1280, 720)
    ex.show()


    app.setStyleSheet(qdarktheme.load_stylesheet("light"))

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
