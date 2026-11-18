from astronomy.time_calculations import get_mean_obliquity
import pytest

# python -m pytest tests/test_get_mean_obliquity.py -v

@pytest.mark.parametrize(
    "julian_day, expected",
    [
        (2451545.0, 23.4392911111), # siècle julien = 0
        (36525 + 2451545.0, 23.4262872841) # siècle julien = 1

    ]
)

def test_get_mean_obliquity(julian_day, expected):
    result = get_mean_obliquity(julian_day)
    assert result == pytest.approx(expected)