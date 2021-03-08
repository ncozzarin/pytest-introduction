import pytest
from accum import Accumulator
#this fixture function creates accumulator objects
@pytest.fixture
def accum():
    return Accumulator()

@pytest.fixture
def accum2():
    return Accumulator()

def test_accumulator_init(accum,accum2):
    assert accum.count == 0

def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

