import math

def get_ascendant_and_descendant(
    local_sidereal_angle: float,
    latitude: float,
    mean_obliquity: float
) -> tuple[float, float]:

    """
    Calcule les longitudes écliptiques de l'Ascendant (ASC)
    et du Descendant (DSC).

    Args:
        local_sidereal_angle (float): Angle sidéral local en radians.
        latitude (float): Latitude géographique en degrés.
        mean_obliquity (float): Obliquité moyenne de l'écliptique en degrés.

    Returns:
        tuple[float, float]: Longitudes écliptiques de l'Ascendant
            et du Descendant en degrés, dans cet ordre.

    Notes:
        - Les calculs trigonométriques sont effectués en radians.
        - Le Descendant est situé à 180° de l'Ascendant.
        - Les longitudes retournées sont normalisées dans [0°, 360°[.
    """

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


def get_declination(ecliptic_longitude:float, mean_obliquity:float)->float:
    """
    Calcule la déclinaison d'un point situé sur l'écliptique.

    δ = arcsin(sin(ε) * sin(λ))

    - ε (obliquité) : mean_obliquity
    - λ (longitude écliptique) : ecliptic_longitude
    - δ (déclinaison) : declination

    Args:
        ecliptic_longitude (float): Longitude écliptique en degrés.
        mean_obliquity (float): Obliquité moyenne en degrés.

    Returns:
        float: Déclinaison en degrés, comprise entre -90 et +90.

    Notes:
        Les calculs intermédiaires sont effectués en radians.
        La latitude écliptique du point est supposée nulle.
        La déclinaison peut être négative.
    """

    ecliptic_longitude_rad = math.radians(ecliptic_longitude)
    mean_obliquity_rad = math.radians(mean_obliquity)

    declination_rad = math.asin(math.sin(mean_obliquity_rad) * math.sin(ecliptic_longitude_rad))
    # Attention : contrairement aux longitudes écliptiques, la déclinaison peut être négative. 
    # Il ne faudra donc surtout pas appliquer de % 360 à notre résultat.

    declination = math.degrees(declination_rad)

    return declination


def get_right_ascension(ecliptic_longitude:float, mean_obliquity:float):

    """Calcule l'ascension droite d'un point situé sur l'écliptique.

    α = atan2(sin(λ) * cos(ε), cos(λ))

    - α : ascension droite
    - λ : longitude écliptique
    - ε : obliquité de l'écliptique

    Args:
        ecliptic_longitude (float): Longitude écliptique en degrés.
        mean_obliquity (float): Obliquité moyenne en degrés.

    Returns:
        float: Ascension droite en degrés, dans l'intervalle [0, 360[.

    Notes:
        La formule suppose une latitude écliptique nulle.
        Les calculs trigonométriques sont effectués en radians.
        Le modulo 360 est appliqué après la conversion en degrés.
    """

    ecliptic_longitude_rad = math.radians(ecliptic_longitude)
    mean_obliquity_rad = math.radians(mean_obliquity)

    right_ascension_rad = math.atan2(math.sin(ecliptic_longitude_rad) * math.cos(mean_obliquity_rad), math.cos(ecliptic_longitude_rad))
    right_ascension = math.degrees(right_ascension_rad) % 360

    return right_ascension


def get_diurnal_semi_arc(latitude: float, declination:float) -> float:

    """Calcule le semi-arc diurne.

    H₀ = arccos(-tan(φ) * tan(δ))

    - H₀ : semi-arc diurne
    - φ : latitude géographique
    - δ : déclinaison

    Args:
        latitude (float): Latitude géographique en degrés.
        declination (float): Déclinaison en degrés.

    Returns:
        float: Semi-arc diurne en degrés, compris entre 0 et 180.

    Raises:
        ValueError: Si le point ne se lève pas ou ne se couche
            pas, hors tolérance numérique.

    Notes:
        Les angles sont convertis en radians pour les calculs
        trigonométriques.
        Les dépassements des bornes de l'arccosinus inférieurs
        ou égaux à la tolérance absolue de 1e-12 sont corrigés.
        Les valeurs 0° et 180° correspondent à des cas limites.
    """

    latitude_rad = math.radians(latitude)
    declination_rad = math.radians(declination)

    argument = -math.tan(latitude_rad) * math.tan(declination_rad)

    if argument > 1 and math.isclose(argument, 1, rel_tol=0, abs_tol=1e-12):
        argument = 1
    if argument < -1 and math.isclose(argument, -1, rel_tol=0, abs_tol=1e-12):
        argument = -1

    if not -1 <= argument <= 1:
        raise ValueError("Semi-arc diurne non défini : le point ne se lève pas ou ne se couche pas.")

    diurnal_semi_arc_rad = math.acos(argument)
    diurnal_semi_arc = math.degrees(diurnal_semi_arc_rad)
    return diurnal_semi_arc


# math.acos() : l'arccosinus.
# L'arccosinus, comme l'arcsinus, n'accepte que des valeurs comprises entre −1 et +1.
# Expression	Résultat
# arccos(−1)	180°
# arccos(−0,5)	120°
# arccos(0)	    90°
# arccos(0,5)	60°
# arccos(1)	    0°
# arccos(1,5)	Impossible
# Et c'est précisément ici que se cache l'une des grandes limitations géographiques de Placidus.
# Aux latitudes élevées, certains points de l'écliptique peuvent ne jamais se lever ou ne jamais se coucher. 
# Notre expression peut alors sortir de l'intervalle autorisé.

# Dans notre fonction, nous allons donc décomposer la formule en deux étapes.
# Étape 1 : calculer l'argument de l'arccosinus.
# Étape 2 : vérifier sa validité avant de calculer le semi-arc diurne.

# Trois situations peuvent se présenter :
# Valeur de A	Conséquence astronomique
# A inférieur à −1	Le point reste au-dessus de l'horizon.
# A compris entre −1 et +1	Le calcul est mathématiquement possible.
# A supérieur à +1	Le point reste sous l'horizon.
# Les valeurs exactement égales à −1 ou +1 correspondent à des cas limites où le point effleure l'horizon.
# Dans ASTROLOGIK, nous devrons donc intercepter les valeurs hors domaine pour éviter que le calcul de Placidus ne fasse planter tout le programme.


def get_nocturnal_semi_arc(latitude: float, declination: float, diurnal_semi_arc) -> float:

    """Calcule le semi-arc nocturne.

    Hₙ = 180° - H₀

    - H₀ : semi-arc diurne
    - Hₙ : semi-arc nocturne

    Args:
        latitude (float): Latitude géographique en degrés.
        declination (float): Déclinaison en degrés.

    Returns:
        float: Semi-arc nocturne en degrés, compris entre 0 et 180.

    Raises:
        ValueError: Si le semi-arc diurne n'est pas défini.

    Notes:
        Réutilise get_diurnal_semi_arc() pour calculer H₀.
    """

    # Situation 	             Semi-arc diurne	     Semi-arc nocturne
    # Équinoxe	                     90°	                90°
    # Journée longue	             110°	                70°
    # Journée courte	             70°	                110°
    # Cas limite jour polaire	     180°	                0°
    # Cas limite nuit polaire	     0°	                    180°

    nocturnal_semi_arc = 180 - diurnal_semi_arc
    return nocturnal_semi_arc







