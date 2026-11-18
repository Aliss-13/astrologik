from astronomy.time_calculations import get_local_sidereal_time
import pytest

# python -m pytest tests/test_get_local_sidereal_time.py -v

@pytest.mark.parametrize(
    "julian_day, longitude, expected",
    [
        (2451545.0, 30, 20.697374558), # 30° Est : le temps sidéral local augmente.
        (2451545.0, -30, 16.697374558), # 30° Ouest : le temps sidéral local diminue.
        (2451545.0, 90, 0.6973745579999999) # 90° Est : le calcul franchit minuit et revient correctement dans l'intervalle de 0 à 24 h.
    ]
)

def test_get_local_sidereal_time(julian_day, longitude, expected):
    result = get_local_sidereal_time(julian_day, longitude)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize(
    "julian_day, longitude, expected",
    [
        (2460677.0, 30, 20 + 45/60 + 34.1703/3600), # 30° Est : le temps sidéral local augmente.
        (2460677.0, -30, 16 + 45/60 + 34.1703/3600), # 30° Ouest : le temps sidéral local diminue.
        (2460677.0, 90, 0 + 45/60 + 34.1703/3600) # 90° Est : le calcul franchit minuit et revient correctement dans l'intervalle de 0 à 24 h.
    ]
)

def test_lst_astronomical_reference(julian_day, longitude, expected):
    """Comparaison avec l'US Naval Observatory.
    Source : https://aa.usno.navy.mil/data/siderealtime
    - Utilisation du temps sidéral local moyen (TSLM ou LMST).
    - Réserve : les références sont en UT1, tandis que notre
      calcul assimile provisoirement UTC à UT1.
    """
    lst = get_local_sidereal_time(julian_day, longitude)
    assert lst == pytest.approx(expected, abs=0.01/3600, rel=0)