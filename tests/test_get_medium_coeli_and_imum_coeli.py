import pytest
import math

from astronomy.coordinates import get_medium_coeli_and_imum_coeli

# python -m pytest tests/test_get_medium_coeli_and_imum_coeli.py -v

@pytest.mark.parametrize(
    "local_sidereal_angle, mean_obliquity, mc_expected, ic_expected",
    [
        (0, 23.44, 0, 180),
        (math.radians(90), 23.44, 90, 270),
        (math.radians(270), 23.44, 270, 90),
        (math.radians(45), 23.44, 47.46432956190184, 227.46432956190185)

    ]
)

def test_get_medium_coeli_and_imum_coeli(local_sidereal_angle, mean_obliquity, mc_expected, ic_expected):
    medium_coeli, imum_coeli = get_medium_coeli_and_imum_coeli(local_sidereal_angle, mean_obliquity)
    assert medium_coeli == pytest.approx(mc_expected)
    assert imum_coeli == pytest.approx(ic_expected)