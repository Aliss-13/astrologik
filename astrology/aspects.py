from itertools import combinations
# combinations(positions, 2) signifie : « Génère toutes les combinaisons de deux clés distinctes du dictionnaire, 
# sans tenir compte de leur ordre. »
from astrology.geometry import angular_distance


ANGLES = {
    "Conjonction": 0,
    "Sextile": 60,
    "Carré": 90,
    "Trigone": 120,
    "Opposition": 180
}

def find_aspect(distance, orb):

    for aspect, angle in ANGLES.items():
        if distance-orb <= angle <= distance+orb:
            return aspect

    return None


def get_planetary_aspects(positions, orb):

    aspects = []

    for planet_1, planet_2 in combinations(positions, 2):
        longitude_1 = positions[planet_1]
        longitude_2 = positions[planet_2]

        distance = angular_distance(longitude_1, longitude_2)
        aspect = find_aspect(distance, orb)

        if aspect is not None:
            #  à déplacer dans le main

            aspects.append(
                {"planet_1": planet_1, 
                "planet_2": planet_2, 
                "aspect": aspect, 
                "distance": distance}
                )
        
    return aspects


