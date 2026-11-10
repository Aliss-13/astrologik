import requests
from datetime import datetime, timedelta

PLANETS = {
    "Soleil": "10",
    "Lune": "301",
    "Mercure": "199",
    "Vénus": "299",
    "Mars": "499",
    "Jupiter": "599",
    "Saturne": "699",
    "Uranus": "799",
    "Neptune": "899",
    "Pluton": "999"
}

# python -m api.astronomy

def get_planet_position(planet_id, start_time):

    date = datetime.strptime(start_time, "%Y-%m-%d %H:%M") # Cette méthode transforme une chaîne de caractères en objet datetime.
    date_end = date + timedelta(hours=1) # calculer une date de fin exactement une heure après la date de départ
    time_end = date_end.strftime("%Y-%m-%d %H:%M") # Cette méthode transforme un objet datetime en une chaîne de caractères.

    url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    params = {
        "format": "json",
        "COMMAND": planet_id, 
        "QUANTITIES": "31",
        "CENTER": "500@399",
        "EPHEM_TYPE": "OBSERVER",
        "START_TIME": start_time,
        "STOP_TIME": time_end,
        "STEP_SIZE": "1 h"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if "error" in data:
            print("Erreur Horizons :", data["error"])
            return
        
        parties = data["result"].split("$$SOE")
        ephemerides = parties[1].split("$$EOE")[0]
        
        lines = ephemerides.strip().split("\n")
        
        longitude = float(lines[0].split()[2])
        
        return longitude

    except requests.exceptions.Timeout:
        print("La NASA prend son café. Réessayez plus tard ! ☕")

    # print(response.status_code) # HTTP : le serveur a t-il correctement répondu ?
    # print(type(response)) # La réponse contient-elle les données astrologiques attendues ?
    # print(response.text)

def get_all_planets_positions(start_time):

    positions = {}

    for planet_name, planet_id in PLANETS.items():
        planet_position = get_planet_position(planet_id, start_time)
        positions[planet_name] = planet_position

    return positions