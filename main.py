import socket

HOST = "localhost"
PORT = 5000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server running at http://{HOST}:{PORT}")
    
    while True:
        client_socket, addr = server.accept()
        with client_socket:
            request = client_socket.recv(1024)
            response_body = "Hello, World!"
            headers = [
                "HTTP/1.1 200 OK",
                f"Host: {HOST}:{PORT}",
                "Content-Type: text/plain",
                f"Content-Length: {len(response_body)}",
                "Connection: close",
            ]
            response = "\r\n".join(headers).encode("utf-8") + b"\r\n\r\n" + response_body.encode("utf-8")
            client_socket.sendall(response)
