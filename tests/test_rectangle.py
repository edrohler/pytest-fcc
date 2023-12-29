import pytest
import source.shapes as shapes

def test_area(rectangle):
    assert rectangle.area() == 200
    
def test_perimeter(rectangle):
    assert rectangle.perimeter() == 60
    
def test_not_equal(rectangle, rectangle2):
    assert rectangle != rectangle2