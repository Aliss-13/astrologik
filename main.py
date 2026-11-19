from display import (astro_logik_presentation, display_planet_positions, display_planetary_aspects, display_available_cities, 
                     display_double_calculation_message, display_ascendant_and_descendant, display_sun_position,
                     display_medium_coeli_and_imum_coeli)

from user_input import get_date_and_time, get_city_data, get_city_name, ask_ambiguous_time
from dates_and_time import get_timezone, convert_to_utc, analyze_local_time

from api.astronomy import get_all_planets_positions
from api.geography import search_cities

from astrology.aspects import get_planetary_aspects

from astronomy.time_calculations import (get_julian_day, get_mean_obliquity, get_local_sidereal_time, 
                                         get_local_sidereal_angle_radians)
from astronomy.coordinates import get_ascendant_and_descendant, get_medium_coeli_and_imum_coeli

from datetime import datetime


# Choix ville
def city_choice():

    city = get_city_name() # Saisie utilisateur ville recherchée
    if not city:
        return

    available_cities = search_cities(city) # Recherche
    if not available_cities:
        print("Aucune ville ne correspond.")
        return

    display_available_cities(available_cities) # Affichage des villes trouvées

    chosen_city = get_city_data(available_cities) # Sélection de l'utilisateur parmi les villes trouvées
    if not chosen_city:
        return

    print(f"Ville choisie : {chosen_city['display_name']}")

    latitude = float(chosen_city["lat"])
    longitude = float(chosen_city["lon"])

    coordinates = latitude, longitude
    return coordinates


def main():

    # Présentation
    astro_logik_presentation()


    # Récupération date et heure locales
    start_time = get_date_and_time()
    if not start_time:
        return


    # Récupération ville avec info latitude, longitude
    coordinates = city_choice()
    if not coordinates:
        return
    
    latitude, longitude = coordinates


    # Récupération fuseau horaire
    timezone_name = get_timezone(latitude, longitude)
    if not timezone_name:
        return

    
    # Conversion utc
    time_status, date_first, date_second = analyze_local_time(start_time, timezone_name)

    choice = None

    if time_status == "non_existent_time":
        print("Heure inexistante.")
        return

    if time_status == "ambiguous_time":
        choice = ask_ambiguous_time()
        if choice == "3":
            display_double_calculation_message()

    start_times_utc = convert_to_utc(time_status, date_first, date_second, choice)

    print(f"Fuseau horaire : {timezone_name}")
    print(f"Heure locale : {start_time}")


    orb = 5

    for start_time_utc_item in start_times_utc:

        # Récupération des données : position des planètes
        positions = get_all_planets_positions(start_time_utc_item)

        # Affichage : signe solaire
        display_sun_position(positions)
        
        # Calcul de l'ascendant et du descendant
        date_utc = datetime.strptime(start_time_utc_item, "%Y-%m-%d %H:%M")
        julian_day = get_julian_day(date_utc.day, date_utc.month, date_utc.year, 
                                    date_utc.hour, date_utc.minute, date_utc.second)
        mean_obliquity = get_mean_obliquity(julian_day)
        local_sidereal_time = get_local_sidereal_time(julian_day, longitude)
        local_sidereal_angle_radians = get_local_sidereal_angle_radians(local_sidereal_time)
        ascendant, descendant = get_ascendant_and_descendant(local_sidereal_angle_radians, latitude, mean_obliquity)

        # Affichage : ascendant et descendant
        display_ascendant_and_descendant(ascendant, descendant)

        # Calcul : Milieu du Ciel, Fond du Ciel
        medium_coeli, imum_coeli = get_medium_coeli_and_imum_coeli(local_sidereal_angle_radians, mean_obliquity)

        # Affichage : Milieu du Ciel, Fond du Ciel
        display_medium_coeli_and_imum_coeli(medium_coeli, imum_coeli)

        # Affichage : position des planètes
        display_planet_positions(positions, start_time, start_time_utc_item)

        # Calcul des aspects pour chaque "positions"
        aspects = get_planetary_aspects(positions, orb)

        # Affichage : aspects des planètes
        display_planetary_aspects(aspects)

        

if __name__ == "__main__":
    main()