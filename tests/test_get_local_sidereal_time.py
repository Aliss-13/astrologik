from astronomy.time_calculations import get_local_sidereal_time
import pytest

# python -m pytest tests/test_get_local_sidereal_time.py -v

@pytest.mark.parametrize(
    "greenwich_sidereal_time, longitude, expected",
    [
        (10, 30, 12),
        (23, 45, 2),
        (1, -45, 22),
        (10, 10, 10.666666666666666),
        (23, 15, 0)
    ]
)

def test_get_local_sidereal_time(greenwich_sidereal_time, longitude, expected):

    # TSL = TSG + (longitude/15)
    # - TSL : temps sidéral local, exprimé en heures.
    # - TSG : temps sidéral de Greenwich, exprimé en heures.
    # - Longitude : positive vers l'est, négative vers l'ouest.
    # On ramène ensuite le résultat entre 0 et 24 heures.

    result = get_local_sidereal_time(greenwich_sidereal_time, longitude)

    assert result == pytest.approx(expected)