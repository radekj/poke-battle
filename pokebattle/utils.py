from functools import wraps

from sqlalchemy.util._collections import AbstractKeyedTuple


def dictify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not result:
            return None
        elif isinstance(result, list):
            return [row_to_dict(row) for row in result]
        return row_to_dict(result)
    return wrapper


def row_to_dict(row):
    if isinstance(row, AbstractKeyedTuple):
        return row._asdict()
    return dict([
        (column.name, str(getattr(row, column.name)))
        for column in row.__table__.columns])
