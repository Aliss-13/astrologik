from astronomy.time_calculations import get_julian_day
import pytest

# python -m pytest tests/test_get_julian_day.py -v

@pytest.mark.parametrize(
    "day, month, year, hour, minute, second, expected",
    [
        (1, 1, 2000, 0, 0, 0, 2451544.5),
        (1, 1, 2000, 12, 0, 0, 2451545.0),
        (1, 1, 2000, 6, 30, 0, 2451544.5 + 6.5/24),
        (28, 2, 2000, 0, 0, 0, 2451602.5),
        (29, 2, 2000, 0, 0, 0, 2451603.5),
        (1, 3, 2000, 0, 0, 0, 2451604.5),
        (28, 2, 1900, 0, 0, 0, 2415078.5),
        (1, 3, 1900, 0, 0, 0, 2415079.5)

    ]
)

def test_get_julian_day(day, month, year, hour, minute, second, expected):
    julian_day = get_julian_day(day, month, year, hour, minute, second)
    assert julian_day == pytest.approx(expected)