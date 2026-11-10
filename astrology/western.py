def get_zodiac_sign(longitude):

    astrological_signs = [
        "Bélier", "Taureau", "Gémeaux", "Cancer",
        "Lion", "Vierge", "Balance", "Scorpion",
        "Sagittaire", "Capricorne", "Verseau", "Poissons"
    ]

    longitude = longitude % 360

    sector = int(longitude // 30)

    astrological_sign = astrological_signs[sector]

    return astrological_sign