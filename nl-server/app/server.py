import os
import socket
import threading
from typing import Tuple
from app.protocol import parse_line, encode_ok, encode_err
from app.handlers import handle_command
from app.store import InMemoryStore

DEFAULT_HOST = os.environ.get("SERVER_HOST", "0.0.0.0")
DEFAULT_PORT = int(os.environ.get("SERVER_PORT", "5050"))

class ClientThread(threading.Thread):
    def __init__(self, onn: socket.socket, addr:Tuple[str, int], store: InMemoryStore):
        super().__init__(daemon=True)
        self.conn = conn
        self.addr = addr
        self.store = store
        self.rfile= self.conn.makefile("r", enconding="utf-8", newline="\n")
        self.wfile= self.conn.makefile("w", enconding="utf-8", newline="\n")

    def log(self, msg: str):
        print(f"[{self.addr[0]}: {self.addr[1]}] {msg}")

    def send(self, msg: str):
        self.wfile.write(line + "\n")
        self.wfile.flush()

    def run 


class Server:
    def __init__(self, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT):
        self.host = host
        self.port = port
        self.store = InMemoreStore()

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen()
            print(f"[server] listening on {self.host}: {self.port}")
            while True: ### TODO: CHANGE !!!!
                conn, addr = s.accept()
                t = ClientThread(conn, addr, self.store)
                t.start()

if __name__ == "__main__":
    Server().run()
