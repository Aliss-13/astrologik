from astronomy.coordinates import get_diurnal_semi_arc
import math

import pytest

# python -m pytest tests/test_get_diurnal_semi_arc.py -v

# -s affiche les print

@pytest.mark.parametrize(
    "latitude, declination, expected",
    [
        (0, 0, 90),
        (0, 23.44, 90),
        (0, -23.44, 90),
        (45, 0, 90),
        (45, 45, 180),
        (45, -45, 0),
    ]
)

def test_get_diurnal_semi_arc(latitude, declination, expected):
    diurnal_semi_arc = get_diurnal_semi_arc(latitude, declination)
    assert diurnal_semi_arc == pytest.approx(expected, rel=0, abs=1/100000) # 1/100000 = 1e-5

@pytest.mark.parametrize(
    "latitude, declination",
    [
        (80, 23.44), # arccos(-2.458888)
        (80, -23.44) # arccos(2.458888)
    ]
)

def test_get_diurnal_semi_arc_invalid_domain(latitude, declination):

    with pytest.raises(ValueError, match="Semi-arc diurne non défini : le point ne se lève pas ou ne se couche pas."):
        get_diurnal_semi_arc(latitude, declination)


@pytest.mark.parametrize(
    "first_tan, second_tan, expected",
    [
        (1.0, -1.0000000000000002, 0),
        (1.0, 1.0000000000000002, 180)
    ]
)

def test_get_diurnal_semi_arc_rounding(first_tan, second_tan, monkeypatch, expected):

    values = iter([first_tan, second_tan])

    def fake_tan(angle):
        return next(values)

    monkeypatch.setattr(math, "tan", fake_tan)

    diurnal_semi_arc = get_diurnal_semi_arc(45, -45)
    assert diurnal_semi_arc == expected
