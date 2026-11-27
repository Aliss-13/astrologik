from astronomy.coordinates import get_right_ascension

import pytest

# python -m pytest tests/test_get_right_ascension.py -v

@pytest.mark.parametrize(
    "ecliptic_longitude, mean_obliquity, expected",
    [
        (0, 23.44, 0),
        (90, 23.44, 90),
        (180, 23.44, 180),
        (270, 23.44, 270),
        (45, 23.44, 42.53567043809815),
        (315, 23.44, 317.4643295619019),
        
    ]
)

def test_get_right_ascension(ecliptic_longitude, mean_obliquity, expected):
    right_ascension = get_right_ascension(ecliptic_longitude, mean_obliquity)
    assert right_ascension == pytest.approx(expected)