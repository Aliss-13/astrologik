from datetime import datetime, timezone

from zoneinfo import ZoneInfo

from timezonefinder import TimezoneFinder
tf = TimezoneFinder()


def convert_to_utc(time_status, date_first, date_second, choice=None):

    dates_to_process = []

    # Traitement de results
    if time_status == "ambiguous_time":
        
        if choice == "1":
            dates_to_process.append(date_first.astimezone(timezone.utc))
            
        elif choice == "2":
            dates_to_process.append(date_second.astimezone(timezone.utc))
            
        elif choice == "3":
            dates_to_process.extend([date_first.astimezone(timezone.utc), date_second.astimezone(timezone.utc)])

    elif time_status == "non_existent_time":
        return

    else:
        dates_to_process.append(date_first.astimezone(timezone.utc)) 

    # Traitement de dates_to_process
    start_times_utc = []

    for date in dates_to_process:
        date_str = date.strftime("%Y-%m-%d %H:%M")
        # dans astronomy.py, get_planet_position() fait déjà date = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        # Elle attend donc toujours une chaîne de caractères.
        # Si tu lui transmets un objet datetime, Python déclenchera une TypeError.
        # => Pour vérifier la validité de la saisie, pas besoin de réaffecter start_time
        start_times_utc.append(date_str)

    # Retour des start_times_utc
    return start_times_utc


def get_timezone(latitude, longitude):
    timezone = tf.timezone_at(lat = latitude, lng = longitude)
    return timezone


def helper_offsets_are_the_same(offset_first, offset_second):
    return offset_first == offset_second # return True par défaut


def detect_time_status(results, offset_first, offset_second, date_first, date_second):

    if results == [True, True] and not helper_offsets_are_the_same(offset_first, offset_second):
        return "ambiguous_time", date_first, date_second

    elif results == [False, False]:
        return "non_existent_time", None, None

    elif results == [True, True] and helper_offsets_are_the_same(offset_first, offset_second):
        return "normal_time", date_first, None


def analyze_local_time(start_time, timezone_name):

    date_local = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    
    date_first = date_local.replace(tzinfo=ZoneInfo(timezone_name), fold=0)
    date_second = date_local.replace(tzinfo=ZoneInfo(timezone_name), fold=1)
    
    offset_first = date_first.utcoffset()
    offset_second = date_second.utcoffset()

    results = []

    for date in (date_first, date_second):
        date_utc = date.astimezone(timezone.utc)
        date_back = date_utc.astimezone(ZoneInfo(timezone_name))
        date_back_naive = date_back.replace(tzinfo=None)
    
        results.append(date_local == date_back_naive)

    return detect_time_status(results, offset_first, offset_second, date_first, date_second)