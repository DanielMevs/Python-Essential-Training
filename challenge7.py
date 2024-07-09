class NonIntArgumentException(Exception):
    pass


def handleNonIntArguments(func):
    def wrapper(*args):
        for item in args:
            if not isinstance(item, int):
                raise NonIntArgumentException()
        return func(*args)
    return wrapper