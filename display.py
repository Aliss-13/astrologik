from astrology.zodiac import get_zodiac_sign, get_zodiac_sign_degree

ARROW_RIGHT = "\U0001f816"  # Droite (🠖)
ARROW_LEFT = "\U0001f814"   # Gauche (🠔)
ARROW_UP = "\U0001f815"     # Haut (🠕)
ARROW_DOWN = "\U0001f817"   # Bas (🠗)

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
MAGENTA = "\033[38;2;218;80;190m"
LAVENDER = "\033[38;2;180;154;255m"
SILVER = "\033[38;2;192;192;192m"
RESET = "\033[0m"

ASPECT_COLORS = {
    "Conjonction": MAGENTA,
    "Sextile": BLUE,
    "Carré": RED,
    "Trigone": BLUE,
    "Opposition": RED
}

PLANET_COLORS = {
    "Soleil": "\033[38;2;255;215;0m",      # Or
    "Lune": "\033[38;2;192;192;192m",      # Argent
    "Mercure": "\033[38;2;169;169;169m",   # Gris
    "Vénus": "\033[38;2;144;238;144m",     # Vert clair
    "Mars": "\033[38;2;220;60;60m",        # Rouge
    "Jupiter": "\033[38;2;100;149;237m",   # Bleu royal clair
    "Saturne": "\033[38;2;112;112;112m",   # Gris foncé
    "Uranus": "\033[38;2;64;224;208m",     # Turquoise
    "Neptune": "\033[38;2;147;112;219m",   # Violet
    "Pluton": "\033[38;2;178;34;80m"       # Bordeaux
}

ZODIAC_SYMBOLS = {
    "Bélier": "♈",
    "Taureau": "♉",
    "Gémeaux": "♊",
    "Cancer": "♋",
    "Lion": "♌",
    "Vierge": "♍",
    "Balance": "♎",
    "Scorpion": "♏",
    "Sagittaire": "♐",
    "Capricorne": "♑",
    "Verseau": "♒",
    "Poissons": "♓"
}

PLANET_SYMBOLS = {
    "Soleil": "☉",
    "Lune": "☽",
    "Mercure": "☿",
    "Vénus": "♀",
    "Mars": "♂",
    "Jupiter": "♃",
    "Saturne": "♄",
    "Uranus": "♅",
    "Neptune": "♆",
    "Pluton": "♇"
}

ASPECT_SYMBOLS = {
    "Conjonction": "☌",
    "Sextile": "⚹",
    "Carré": "□",
    "Trigone": "△",
    "Opposition": "☍"
}

def astro_logik_presentation():

    print()
    print(f"                 ๑{CYAN} ~ * · ~ {RESET}☆{CYAN} ~ ° ¯ ° {RESET}Astro--Logik {CYAN}° ¯ ° ~ {RESET}☆{CYAN} ~ · * · ~ {RESET}๑")
    print()
    print(f"{CYAN}Des calculs astronomiques irréprochables au service d'interprétations parfaitement invérifiables.{RESET}")
    print()


def display_planet_positions(positions, start_time, start_time_utc):
    
    print("⌚ Heure saisie :", start_time)
    print("🌐 Heure UTC :", start_time_utc)
    print()
    print(f"------------ Position des planètes ------------")
    print()

    for planet_name, planet_position in positions.items():
        if planet_position is not None:
            zodiac_sign = get_zodiac_sign(planet_position)
            zodiac_sign_degree = get_zodiac_sign_degree(planet_position)
            zodiac_symbol = ZODIAC_SYMBOLS[zodiac_sign]
            planet_symbol = PLANET_SYMBOLS[planet_name]
            planet_color = PLANET_COLORS[planet_name]
            print(f"{planet_color}{planet_symbol} {planet_name:<10}{RESET} {zodiac_sign:<12} {zodiac_symbol} {DIM}{zodiac_sign_degree:>6.2f}°{RESET}") # :.2f arrondit à 2 décimales


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
        aspect_symbol = ASPECT_SYMBOLS[aspect]

        aspect_color = ASPECT_COLORS[aspect]
        planet_1_color = PLANET_COLORS[planet_1]
        planet_2_color = PLANET_COLORS[planet_2]

        print(f"{planet_1_color}{planet_1:<8}{RESET} . {planet_2_color}{planet_2:<8}{RESET} {aspect_color}{aspect_symbol} {aspect:<12}{RESET} {DIM}({distance:>6.2f}° | orbe : {effective_orb:.2f}°){RESET}")


def display_available_cities(available_cities):

    for number, city in enumerate(available_cities, start=1):
        print(f"{number} - {city['display_name']}")


def display_double_calculation_message():
    print("Ben ça va, tranquille, on s'emmerde pas !")
    print()


def display_ascendant_and_descendant(ascendant, descendant):

    zodiac_sign_ascendant = get_zodiac_sign(ascendant)
    zodiac_sign_descendant = get_zodiac_sign(descendant)
    zodiac_sign_ascendant_degree = get_zodiac_sign_degree(ascendant)
    zodiac_sign_descendant_degree = get_zodiac_sign_degree(descendant)
    zodiac_ascendant_symbol = ZODIAC_SYMBOLS[zodiac_sign_ascendant]
    zodiac_descendant_symbol = ZODIAC_SYMBOLS[zodiac_sign_descendant]
    
    print(f"{YELLOW}{ARROW_LEFT} Ascendant : {zodiac_sign_ascendant} {zodiac_ascendant_symbol}{RESET} {DIM}({ascendant:.2f}° | {zodiac_sign_ascendant_degree:.2f}°){RESET}")
    print(f"{SILVER}{ARROW_RIGHT} Descendant : {zodiac_sign_descendant} {zodiac_descendant_symbol}{RESET} {DIM}({descendant:.2f}° | {zodiac_sign_descendant_degree:.2f}°){RESET}")
    print()


def display_medium_coeli_and_imum_coeli(medium_coeli, imum_coeli):

    zodiac_sign_mc = get_zodiac_sign(medium_coeli)
    zodiac_sign_ic = get_zodiac_sign(imum_coeli)
    zodiac_sign_mc_degree = get_zodiac_sign_degree(medium_coeli)
    zodiac_sign_ic_degree = get_zodiac_sign_degree(imum_coeli)
    zodiac_mc_symbol = ZODIAC_SYMBOLS[zodiac_sign_mc]
    zodiac_ic_symbol = ZODIAC_SYMBOLS[zodiac_sign_ic]
    
    print(f"{CYAN}{ARROW_UP} Milieu du Ciel : {zodiac_sign_mc} {zodiac_mc_symbol}{RESET} {DIM}({medium_coeli:.2f}° | {zodiac_sign_mc_degree:.2f}°){RESET}")
    print(f"{SILVER}{ARROW_DOWN} Fond du Ciel : {zodiac_sign_ic} {zodiac_ic_symbol}{RESET} {DIM}({imum_coeli:.2f}° | {zodiac_sign_ic_degree:.2f}°){RESET}")
    print()


def display_sun_position(positions):

    sun_position = positions["Soleil"]
    
    zodiac_solar_sign = get_zodiac_sign(sun_position)
    zodiac_solar_sign_degree = get_zodiac_sign_degree(sun_position)
    zodiac_solar_sign_symbol = ZODIAC_SYMBOLS[zodiac_solar_sign]

    print()
    print(f"{RED}☀️ Signe astrologique : {zodiac_solar_sign}{RESET} {zodiac_solar_sign_symbol} {DIM}({zodiac_solar_sign_degree:.2f}°){RESET}")
    print()