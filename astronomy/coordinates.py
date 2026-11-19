import math

def get_ascendant_and_descendant(local_sidereal_angle, latitude, mean_obliquity):

    # Avec une convention importante :
    #   local_sidereal_angle	    Radians
    #   latitude	                Degrés
    #   mean_obliquity	            Degrés
    # Pourquoi ce mélange ? Parce que tu as déjà créé une fonction qui fournit l'angle sidéral en radians, tandis que nos autres données sont naturellement exprimées en degrés.
    # Nous convertirons donc la latitude et l'obliquité en radians à l'intérieur de get_ascendant(), avant les calculs trigonométriques.

    latitude_rad = math.radians(latitude)
    obliquity_rad = math.radians(mean_obliquity)

    x = -(math.sin(local_sidereal_angle) * math.cos(obliquity_rad) + math.tan(latitude_rad) * math.sin(obliquity_rad))

    y = math.cos(local_sidereal_angle)
  
    ascendant_ecliptic_longitude = math.degrees(math.atan2(y, x)) % 360
    descendant_ecliptic_longitude = (ascendant_ecliptic_longitude + 180) % 360

    return ascendant_ecliptic_longitude, descendant_ecliptic_longitude


def get_medium_coeli_and_imum_coeli(local_sidereal_angle, mean_obliquity):

    obliquity_rad = math.radians(mean_obliquity)

    formula_ecliptic_longitude_medium_coeli = math.atan2(
        math.sin(local_sidereal_angle)/math.cos(obliquity_rad), 
        math.cos(local_sidereal_angle)
        )
    
    medium_coeli = math.degrees(formula_ecliptic_longitude_medium_coeli) % 360

    imum_coeli = (medium_coeli + 180) % 360

    return medium_coeli, imum_coeli