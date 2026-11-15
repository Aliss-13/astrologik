from astrology.western import get_zodiac_sign, get_zodiac_sign_degree


YELLOW = "\033[93m"
CYAN = "\033[38;2;112;198;250m"
BLUE = "\033[94m"
DIM = "\033[2m"
LIGHT_YELLOW = "\033[38;2;255;250;205m"
LIGHT_PINK = "\033[38;5;218m"
LIGHT_GREEN = "\033[38;5;120m"
SOBER_RED = "\033[38;2;212;107;96m"
PURPLE = "\033[95m"
ORANGE = "\033[38;5;208m"
RED = "\033[38;5;196m"
RESET = "\033[0m"


def astro_logik_presentation():

    print()
    print(f"                 ๑{CYAN} ~ * · ~ {RESET}☆{CYAN} ~ ° ¯ ° {RESET}Astro--Logik {CYAN}° ¯ ° ~ {RESET}☆{CYAN} ~ · * · ~ {RESET}๑")
    print()
    print(f"{CYAN}Des calculs astronomiques irréprochables au service d'interprétations parfaitement invérifiables.{RESET}")
    print()


def display_planet_positions(positions, start_time, start_time_utc):
    
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


def display_planetary_aspects(aspects):

    sorted_aspects = sorted(aspects, key=lambda aspect: aspect["effective_orb"])

    print()
    print(f"------------ Aspects planétaires -------------")
    print()

    for aspect_data in sorted_aspects:
        planet_1 = aspect_data["planet_1"]
        planet_2 = aspect_data["planet_2"]
        aspect = aspect_data["aspect"]
        distance = aspect_data["distance"]
        effective_orb = aspect_data["effective_orb"]

        print(f"{planet_1:<8} et {planet_2:<8} : {YELLOW}{aspect:<12}{RESET} ({distance:>6.2f}° | orbe : {effective_orb:.2f}°)")