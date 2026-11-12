from api.astronomy import get_all_planets_positions
from astrology.western import get_zodiac_sign, get_zodiac_sign_degree
from astrology.aspects import get_planetary_aspects
from display import astro_logik_presentation, YELLOW, RESET
from dates_and_time import convert_to_utc


astro_logik_presentation()

while True:

    try:
        start_time = input("Entrez une date et une heure (AAAA-MM-JJ HH:MM) : ")
        timezone_name = "Europe/Paris"
        start_time_utc = convert_to_utc(start_time, timezone_name)
        break # par exemple, au premier essai, strptime() déclenche une ValueError. Au second, la date est valide et break interrompt la boucle.

    except ValueError:
        print("Saisie invalide.")


positions = get_all_planets_positions(start_time_utc)
print()
print("⌚ Heure saisie :", start_time)
print("🌐 Heure UTC :", start_time_utc)
print()
print(f"------------ Position des planètes ------------")
print()

for planet_name, planet_position in positions.items():
     if planet_position is not None:
        zodiac_sign = get_zodiac_sign(planet_position)
        zodiac_sign_degree = get_zodiac_sign_degree(planet_position)
        print(f"{planet_name:<10} : {zodiac_sign:<12} {zodiac_sign_degree:>6.2f}°") # :.2f arrondit à 2 décimales



aspects = get_planetary_aspects(positions, 5)
print()
print(f"------------ Aspects planétaires -------------")
print()

for aspect_data in aspects:
    planet_1 = aspect_data["planet_1"]
    planet_2 = aspect_data["planet_2"]
    aspect = aspect_data["aspect"]
    distance = aspect_data["distance"]

    print(f"{planet_1:<8} et {planet_2:<8} : {YELLOW}{aspect:<12}{RESET} ({distance:>6.2f}°)")


