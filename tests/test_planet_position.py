import pytest
import api.astronomy

# python -m pytest tests/test_planet_position.py -v

@pytest.mark.parametrize(
    "failed_planet_id, expected_name",
    [
        ("10", "Soleil"),
        ("499", "Mars"),
        ("599", "Jupiter")
    ]
)

def test_missing_planet_position(monkeypatch, failed_planet_id, expected_name):

    # Pour simuler la NASA, pytest propose un outil appelé monkeypatch.
    # Il permet de remplacer temporairement une fonction par une autre pendant un test, sans modifier ton véritable programme.
    
    start_time = "2022-01-01 14:00"

    def fake_get_planet_position(planet_id, start_time):
        if planet_id == failed_planet_id:
            return None
        return 253.5

    monkeypatch.setattr(
        api.astronomy,
        "get_planet_position",
        fake_get_planet_position
    )

    # « Dans le module astronomy, remplace temporairement get_planet_position par fake_get_planet_position. »
    # Cette modification sera automatiquement annulée après le test.

    with pytest.raises(ValueError, match=f"La longitude de {expected_name} n'a pas pu être récupérée"):
        
        api.astronomy.get_all_planets_positions(start_time)


def test_all_planets_positions(monkeypatch):
    
    start_time = "2022-01-01 14:00"
    
    called_ids = []

    def fake_get_planet_position(planet_id, start_time):
        called_ids.append(planet_id)
        return 253.5 

    monkeypatch.setattr(
        api.astronomy,
        "get_planet_position",
        fake_get_planet_position
    )

    positions = api.astronomy.get_all_planets_positions(start_time)
    assert called_ids == list(api.astronomy.PLANETS.values())
    assert len(positions) == len(api.astronomy.PLANETS)
    assert positions.keys() == api.astronomy.PLANETS.keys()
   

    for planet_name, longitude in positions.items():
        assert longitude == 253.5

    

    



    