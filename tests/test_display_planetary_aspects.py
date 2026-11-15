from display import display_planetary_aspects

def test_display_planetary_aspects(capsys):

    aspects = [
        {"planet_1": "Soleil", "planet_2": "Mars", "aspect": "Trigone", "distance": 123, "effective_orb": 3}, # Ton trigone avec une orbe de 3°
        {"planet_1": "Vénus", "planet_2": "Jupiter", "aspect": "Sextile", "distance": 61, "effective_orb": 1} # Ton sextile avec une orbe de 1°
    ]

    display_planetary_aspects(aspects)

    captured = capsys.readouterr()

    assert "Trigone" in captured.out # Vérifier la présence des deux aspects
    assert "Sextile" in captured.out # Vérifier la présence des deux aspects
    assert captured.out.find("Sextile") < captured.out.find("Trigone") # Vérifier leur ordre d'affichage