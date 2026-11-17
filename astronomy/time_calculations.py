import math

def get_local_sidereal_time(greenwich_sidereal_time, longitude):

    # TSL = TSG + (longitude/15)
    # - TSL : temps sidéral local, exprimé en heures.
    # - TSG : temps sidéral de Greenwich, exprimé en heures.
    # - Longitude : positive vers l'est, négative vers l'ouest.
    # On ramène ensuite le résultat entre 0 et 24 heures.

    local_sidereal_time = (greenwich_sidereal_time + (longitude/15)) % 24
    return local_sidereal_time


def get_day_fraction(hour, minute, second):
    """Convertit une durée en fraction de journée."""
    day_fraction = hour/24 + minute/1440 + second/86400
    return day_fraction


def get_julian_day(day, month, year, hour, minute, second):

    if month in (1, 2):
        accurate_month = 12 + month
        accurate_year = year - 1 

    else:
        accurate_month = month
        accurate_year = year

    a = accurate_year // 100
    b = 2 - a + a // 4 # Cette variable sert à appliquer la correction du calendrier grégorien dans le calcul du jour julien.

    julian_day = math.floor(365.25*(accurate_year + 4716)) + math.floor(30.6001*(accurate_month + 1)) + day + b - 1524.5

    day_fraction = get_day_fraction(hour, minute, second)

    julian_day_accurate = julian_day + day_fraction

    return julian_day_accurate


def is_leap_year(year):
    """Détermine si l'année est bissextile :
    Une année est bissextile si elle est :
    - divisible par 4 sauf si elle est divisible par 100 ;
    - mais elle redevient bissextile si elle est divisible par 400.
    Par exemple, 2000 était bissextile, mais 1900 ne l'était pas."""

    if year % 4 == 0 and year % 100 != 0:
        return True
    
    if year % 400 == 0:
        return True
    
    return False



