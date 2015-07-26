from functools import wraps


def dictify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not result:
            return None
        if isinstance(result, list):
            return [row._asdict() for row in result]
        return result._asdict()
    return wrapper
