import pytest
from main.stopwatch import Stopwatch


@pytest.fixture
def stopwatch():
    return Stopwatch()


def test_stopwatch_init(stopwatch):
    assert stopwatch.count == 0


def test_stopwatch_add_one(stopwatch):
    stopwatch.add()
    assert stopwatch.count == 1


def test_stopwatch_add_three(stopwatch):
    stopwatch.add(3)
    assert stopwatch.count == 3


def test_stopwatch_add_twice(stopwatch):
    stopwatch.add()
    stopwatch.add()
    assert stopwatch.count == 2


def test_stopwatch_cannot_set_count_directly(stopwatch):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        stopwatch.count = 10


