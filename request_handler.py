from headers import Headers


class RequestHandler(object):

    def __init__(self, *args, **kwargs):
        self.protocol = kwargs.get('protocol')
        self.path = kwargs.get('path')
        self.method = kwargs.get('method')
        self.body = kwargs.get('body')
        self.headers = Headers(**kwargs.get('headers'))
