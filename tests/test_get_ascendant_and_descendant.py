from astronomy.coordinates import get_ascendant_and_descendant

import pytest
import math

# python -m pytest tests/test_get_ascendant_and_descendant.py -v

@pytest.mark.parametrize(
    "local_sidereal_angle, latitude, mean_obliquity, expected_ascendant, expected_descendant",
    [
        (0, 0, 23.44, 90, 270),
        (math.radians(180), 0, 23.44, 270, 90)
    ]
)

def test_get_ascendant_and_descendant(local_sidereal_angle, latitude, mean_obliquity, expected_ascendant, expected_descendant):

    ascendant, descendant = get_ascendant_and_descendant(local_sidereal_angle, latitude, mean_obliquity)
    assert ascendant == pytest.approx(expected_ascendant, abs=0.01/3600, rel=0)
    assert descendant == pytest.approx(expected_descendant, abs=0.01/3600, rel=0)
    
    # abs = 0.01/3600 :
    # - 1 degré = 60 minutes d'arc.
    # - 1 minute d'arc = 60 secondes d'arc. Donc 1 degré = 3600 secondes d'arc.
    # 0.01/3600 représente 0,01 seconde d'arc exprimée en degrés.
    # rel=0 désactive la tolérance relative, pour que seule notre limite explicite soit utilisée.

    
def test_external_reference_get_ascendant_and_descendant():

    ascendant, descendant = get_ascendant_and_descendant(4.906519730481082, 45, 23.436430013838248)
    
    assert ascendant == pytest.approx(21.00, abs=1/60, rel=0)
    assert descendant == pytest.approx(201.00, abs=1/60, rel=0)
    
    # 1/60 représente 1 minute d'arc exprimée en degrés.