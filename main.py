from display import astro_logik_presentation, display_planet_positions, display_planetary_aspects
from dates_and_time import get_date_and_time
from api.astronomy import get_all_planets_positions
from astrology.aspects import get_planetary_aspects

# Présentation
astro_logik_presentation()

# Position des planètes
start_time_utc, start_time = get_date_and_time()
positions = get_all_planets_positions(start_time_utc)
display_planet_positions(positions, start_time, start_time_utc)

# Calcul des aspects
orb = 5
aspects = get_planetary_aspects(positions, orb)
display_planetary_aspects(aspects)


