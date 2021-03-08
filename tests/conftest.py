import pytest
from accum import Accumulator
#this fixture function creates accumulator objects
@pytest.fixture
def accum():
    return Accumulator()