import pytest
import source.shapes as shapes

@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def rectangle2():
    return shapes.Rectangle(5, 30)
