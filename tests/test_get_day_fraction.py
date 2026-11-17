from astronomy.time_calculations import get_day_fraction
import pytest

# python -m pytest tests/test_get_day_fraction.py -v

@pytest.mark.parametrize(
    "hour, minute, second, expected",
    [
        (12, 0, 0, 0.5),
        (6, 30, 0, 6.5/24),
        (0, 0, 0, 0),
        (24, 0, 0, 1),
        (0, 0, 30, 30/86400)
    ]
)

def test_get_day_fraction(hour, minute, second, expected):
    day_fraction = get_day_fraction(hour, minute, second)
    assert day_fraction == pytest.approx(expected)