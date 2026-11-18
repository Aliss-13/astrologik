from astronomy.time_calculations import get_greenwich_sidereal_time
import pytest

# python -m pytest tests/test_get_greenwich_sidereal_time.py -v

@pytest.mark.parametrize(
    "julian_day, expected",
    [
        (2451545.0, 280.46061837/15), # 01/01/2000 12h utc
        (2488070.0, 18.748737334623) # 01/01/2025 12h utc
    ]
)

def test_get_greenwich_sidereal_time_approx(julian_day, expected):
    greenwich_sidereal_time = get_greenwich_sidereal_time(julian_day)
    assert greenwich_sidereal_time == pytest.approx(expected)


@pytest.mark.parametrize(
    "julian_day, expected",
    [
        (2451545.0, 18 + 41/60 + 50.5494/3600), # 01/01/2000 12h utc
        (2460677.0, 18 + 45/60 + 34.1703/3600) # 01/01/2025 12h utc
    ]
)

def test_gmst_astronomical_reference(julian_day, expected):
    """Comparaison avec l'US Naval Observatory 
    https://aa.usno.navy.mil/data/siderealtime
    - Utilisation du temps sidéral de Greenwich moyen (TSGM ou GMST)
    - Réserve : les références sont en UT1, tandis que notre
      calcul assimile provisoirement UTC à UT1."""

    gst = get_greenwich_sidereal_time(julian_day)

    assert gst == pytest.approx(expected, abs=0.01/3600, rel=0)
    
    # abs = 0.01/3600 :
    # - 1 degré = 60 minutes d'arc.
    # - 1 minute d'arc = 60 secondes d'arc. Donc 1 degré = 3600 secondes d'arc.
    # 0.01/3600 représente 0,01 seconde d'arc exprimée en degrés.
    # rel=0 désactive la tolérance relative, pour que seule notre limite explicite soit utilisée.