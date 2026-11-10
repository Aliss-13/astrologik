astrological_signs = [
        "Bélier", "Taureau", "Gémeaux", "Cancer",
        "Lion", "Vierge", "Balance", "Scorpion",
        "Sagittaire", "Capricorne", "Verseau", "Poissons"
    ]

def get_zodiac_sign(longitude):

    longitude = longitude % 360 # position sur le cercle zodiacal complet

    sector = int(longitude // 30) # numéro du signe (de 0 à 11)

    astrological_sign = astrological_signs[sector]

    return astrological_sign


def get_zodiac_sign_degree(longitude):

    longitude = longitude % 360 # position sur le cercle zodiacal complet

    astrological_sign_degree = longitude % 30 # position à l'intérieur du signe

    return astrological_sign_degree