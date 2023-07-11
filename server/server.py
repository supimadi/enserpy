import socket

class Server:
    def __init__(self, host: str, port: int) -> None:
        # Membuat socket, dengan ip dan port yang di berikan
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))

        self.data = None
        self.conn = None

    def start_server(self) -> None:
        print("Starting Server...")

        self.socket.listen() # listen terus terusan
        self.conn, addr = self.socket.accept() # capture, client yang konek ke server

        print(f"Connected By: {addr}")

        #  self.data_thread = threading.Thread(target=self._read_data)
        #  self.data_thread.start()

    def stop_server(self) -> None:
        self.socket.close()

    def read_data(self):
        if not self.conn:
            print("Not Connected!!")
            return

        while True:
            self.data = self.conn.recv(1024) # baca data yang datang sebanyak 1024 bytes
            self.conn.sendall(f"Terima Kasih Hihi: {self.data.decode('UTF-8')}".encode()) # kirim data ke client
            print(self.data.decode("UTF-8")) # decode pesan dari byte ke string

server = Server("127.0.0.1", 6969)

server.start_server()
server.read_data()
server.stop_server()
