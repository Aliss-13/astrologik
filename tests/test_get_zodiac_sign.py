import pytest
from astrology.western import get_zodiac_sign


@pytest.mark.parametrize(
    "longitude, expected",
    [
        (135.5,	"Lion"), (-15, "Poissons"), (345, "Poissons"), (705, "Poissons"), (0, "Bélier"),  (360, "Bélier"),
        (29.999, "Bélier"), (30, "Taureau"), (30.001, "Taureau")
    ]
)

def test_get_zodiac_sign(longitude, expected):

    result = get_zodiac_sign(longitude)
    assert result == expected
