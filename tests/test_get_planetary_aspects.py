import pytest
from astrology.aspects import get_planetary_aspects

# python -m pytest tests/test_get_planetary_aspects.py -v

@pytest.mark.parametrize(
    "positions, expected",
    [
        ({"Soleil": 230, "Mars": 350, "Jupiter": 10}, [{"planet_1": "Soleil", "planet_2": "Mars", "aspect": "Trigone", "distance": 120}]),
        ({"Terre": 10, "Vénus": 20, "Mercure": 30}, [])
    ]
)

def test_get_planetary_aspects(positions, expected):

    result = get_planetary_aspects(positions, 5)

    assert len(result) == len(expected)
    assert result == expected