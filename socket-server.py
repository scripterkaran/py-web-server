import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))
server_socket.listen(5)


def parse_http(http: str):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split(" ")
    headers = dict(line.split(":", maxsplit=1) for line in headers)
    return method, path, protocol, headers, body


def prepare_response(response):
    return response.encode('utf-8')


def view(request) -> str:
    # todo
    return "Hello from View function of MVC framework"


while True:
    connection, address = server_socket.accept()
    http_request = connection.recv(1024).decode('utf-8')
    request = parse_http(http_request)
    response = view(request)
    http_response = prepare_response(response)
    connection.sendall(http_response)
