import pytest
from astrology.aspects import get_planetary_aspects

# python -m pytest tests/test_get_planetary_aspects.py -v

@pytest.mark.parametrize(
    "positions, orb, expected",
    [
        ({"Soleil": 230, "Mars": 350, "Jupiter": 10}, 5, [{"planet_1": "Soleil", "planet_2": "Mars", "aspect": "Trigone", "distance": 120, "effective_orb": 0}]),
        ({"Soleil": 230, "Mars": 347, "Jupiter": 10}, 3, [{"planet_1": "Soleil", "planet_2": "Mars", "aspect": "Trigone", "distance": 117, "effective_orb": 3}]),
        ({"Soleil": 230, "Mars": 347, "Jupiter": 10}, 2, []),
        ({"Terre": 10, "Vénus": 20, "Mercure": 30}, 5, [])
    ]
)

def test_get_planetary_aspects(positions, orb, expected):

    result = get_planetary_aspects(positions, orb)

    assert len(result) == len(expected)
    assert result == expected