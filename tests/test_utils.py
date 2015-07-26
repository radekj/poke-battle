from sqlalchemy.util._collections import KeyedTuple
from pokebattle.utils import dictify


@dictify
def return_none():
    return None


@dictify
def return_single_result():
    return KeyedTuple([1, 2, 3], labels=['one', 'two', 'three'])


@dictify
def return_list_result():
    labels = ['one', 'two', 'three']
    return [
        KeyedTuple([1, 2, 3], labels=labels),
        KeyedTuple([4, 5, 6], labels=labels)
    ]


def test_dictify_decorator_none_results():
    assert return_none() is None


def test_dictify_decorator_single_result():
    result = return_single_result()
    assert result['one'] == 1 and result['two'] == 2 and result['three'] == 3


def test_dictify_decorator_list_result():
    result = return_list_result()
    assert len(result) == 2
    assert result[1]['one'] == 4 and result[1]['three'] == 6
