from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def convert_to_utc(start_time, timezone_name):

    date_local = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    date_with_timezone = date_local.replace(tzinfo=ZoneInfo(timezone_name))
    date_utc = date_with_timezone.astimezone(timezone.utc)
    start_time_utc = date_utc.strftime("%Y-%m-%d %H:%M")

    # dans astronomy.py, get_planet_position() fait déjà date = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    # Elle attend donc toujours une chaîne de caractères.
    # Si tu lui transmets un objet datetime, Python déclenchera une TypeError.
    # => Pour vérifier la validité de la saisie, pas besoin de réaffecter start_time

    return start_time_utc


def get_date_and_time():

    while True:

        try:
            start_time = input("Entrez une date et une heure (AAAA-MM-JJ HH:MM) : ")
            timezone_name = "Europe/Paris"
            start_time_utc = convert_to_utc(start_time, timezone_name)
            return start_time_utc, start_time

        except ValueError:
            print("Saisie invalide.")