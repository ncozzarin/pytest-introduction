"""
Module to test basic accum module
"""
import pytest

from stuff.accum import Accumulator

def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0

def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


