from astrology.houses import get_equal_houses

import pytest

# python -m pytest tests/test_get_equal_houses.py -v

@pytest.mark.parametrize(
    "ascendant, i, expected",
    [
        (350, 1, 20),
        (350, 0, 350),
        (350, 11, 320)
    ]
)

def test_get_equal_houses(ascendant, i, expected):
    houses_longitudes = get_equal_houses(ascendant)
    assert houses_longitudes[i] == expected


def test_houses_longitudes():
    houses_longitudes = get_equal_houses(350)
    assert houses_longitudes == [350, 20, 50, 80, 110, 140, 170, 200, 230, 260, 290, 320]


