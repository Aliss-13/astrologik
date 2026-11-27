from astronomy.coordinates import get_declination

import pytest

# python -m pytest tests/test_get_declination.py -v

@pytest.mark.parametrize(
    "ecliptic_longitude, mean_obliquity, expected",
    [
        (0, 23.44, 0),
        (90, 23.44, 23.44),
        (180, 23.44, 0),
        (270, 23.44, -23.44),
    ]
)

def test_get_declination(ecliptic_longitude, mean_obliquity, expected):
    declination = get_declination(ecliptic_longitude, mean_obliquity)
    assert declination == pytest.approx(expected)