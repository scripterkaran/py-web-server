class Response:

    def __init__(self, status: int, content):
        self.status = status
        self.body = content

    def to_byte(self):
        return (
            f'HTTP/1.1 {self.status} OK\r\n'
            f'Content-Length: {len(self.body)}\r\n'
            f'Content-Type: text/html\r\n'
            '\r\n'
            f'{self.body}'
            '\r\n'
        )
