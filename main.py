from display import (astro_logik_presentation, display_planet_positions, display_planetary_aspects, display_available_cities, 
                     display_double_calculation_message)

from user_input import get_date_and_time, get_city_data, get_city_name, ask_ambiguous_time
from dates_and_time import get_timezone, convert_to_utc, analyze_local_time

from api.astronomy import get_all_planets_positions
from api.geography import search_cities

from astrology.aspects import get_planetary_aspects


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

        # Position des planètes
        positions = get_all_planets_positions(start_time_utc_item)
        display_planet_positions(positions, start_time, start_time_utc_item)

        # Calcul des aspects pour chaque "positions"
        aspects = get_planetary_aspects(positions, orb)
        display_planetary_aspects(aspects)


if __name__ == "__main__":
    main()




