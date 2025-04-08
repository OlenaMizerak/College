import pytest
from app import Figure

def test_shape():
    figure = Figure('circle', 5)
    assert figure.get_shape() == 'circle'

def test_length():
    figure = Figure('circle', 5)
    assert figure.get_length() == 5

def test_invalid_shape():
    with pytest.raises(ValueError):
        Figure('hexagon', 5)

def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure('square', -3)
