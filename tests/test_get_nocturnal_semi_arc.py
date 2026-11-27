from astronomy.coordinates import get_nocturnal_semi_arc

import pytest

# python -m pytest tests/test_get_nocturnal_semi_arc.py -v

# -s affiche les print

@pytest.mark.parametrize(
    "latitude, declination, diurnal_semi_arc, expected",
    [
        (0, 0, 90, 90),
        (0, 23.44, 90, 90),
        (45, 45, 180, 0),
        (45, -45, 0, 180)
    ]
)

def test_get_nocturnal_semi_arc(latitude, declination, diurnal_semi_arc, expected):
    nocturnal_semi_arc = get_nocturnal_semi_arc(latitude, declination, diurnal_semi_arc)
    assert nocturnal_semi_arc == pytest.approx(expected)