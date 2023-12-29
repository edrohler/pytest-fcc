import pytest
import source.shapes as shapes

@pytest.mark.parametrize('side_length, expected_area', [(5,25),(4,16),(9,81)])
def test_multiple_square_areas(side_length, expected_area):
    square = shapes.Square(side_length)
    assert square.area() == expected_area
    
    
@pytest.mark.parametrize('side_length, expected_perimeter', [(5, 20),(3, 12),(4, 16)])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    square = shapes.Square(side_length)
    assert square.perimeter() == expected_perimeter