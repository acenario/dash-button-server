class Networking:
    @staticmethod
    def get_ip_address():
        import socket
        return socket.gethostbyname(socket.gethostname())