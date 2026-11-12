import pytest
from astrology.aspects import find_aspect

# python -m pytest tests/test_find_aspect.py -v

@pytest.mark.parametrize(
    "distance, orb, expected",
    [
        (2, 5, "Conjonction"),
        (58, 5, "Sextile"),
        (92, 5, "Carré"),
        (119, 5, "Trigone"),
        (178, 5, "Opposition"),
        (80, 5, None),
    ]
)

def test_find_aspect(distance, orb, expected):
    result = find_aspect(distance, orb)
    assert result == expected