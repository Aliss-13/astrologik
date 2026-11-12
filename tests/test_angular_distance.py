import pytest
from astrology.geometry import angular_distance

# python -m pytest tests/test_angular_distance.py -v

@pytest.mark.parametrize(
    "longitude_1, longitude_2, expected",
    [
        (350, 10, 20),
        (90, 180, 90),
        (45, 45, 0),
        (23.76, 25.47, 1.71)
    ]
)

def test_angular_distance(longitude_1, longitude_2, expected):
    result = angular_distance(longitude_1, longitude_2)
    assert result == pytest.approx(expected)