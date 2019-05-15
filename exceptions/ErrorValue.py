class ErrorValue(Exception):
    def __init__(self, msg):
        self._msg = msg

    def get_msg(self):
        return self._msg

    def __str__(self):
        return self._msg

