from astrology.houses import get_porphyre_houses

import pytest

# python -m pytest tests/test_get_porphyre_houses.py -v

@pytest.mark.parametrize(
    "ascendant, ic, descendant, mc, expected",
    [
        (210, 300, 30, 120, [210, 240, 270, 300, 330, 0, 30, 60, 90, 120, 150, 180]), # quadrants de 90°
        (210, 270, 30, 90, [210, 230, 250, 270, 310, 350, 30, 50, 70, 90, 130, 170]), # quadrants 60°/120°
        (210, 310, 30, 130, [210, 210 + 100/3, 210 + 200/3, 310, 310 + 80/3, 3 + 1/3, 30, 30 + 100/3, 30 + 200/3, 130, 130 + 80/3, 130 + 160/3]) # Quadrants de 100°/80° : pas non entiers (divisions par 3)
    ]
)

def test_get_porphyre_houses(ascendant, ic, descendant, mc, expected):
    houses_longitudes = get_porphyre_houses(ascendant, ic, descendant, mc)
    assert houses_longitudes == pytest.approx(expected)