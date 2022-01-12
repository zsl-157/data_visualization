class BaseExceptionss(Exception):
    def __init__(self,message):
        self.msg = message

    def __str__(self):
        return str(self.msg)

    def __repr__(self):
        return str(self.msg)
