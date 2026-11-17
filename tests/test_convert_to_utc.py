import pytest
from dates_and_time import convert_to_utc, analyze_local_time


# python -m pytest tests/test_convert_to_utc.py -v


@pytest.mark.parametrize( # À retenir : un décorateur agit sur la fonction qui le suit, pas sur toutes les fonctions du fichier.
    "start_time, timezone_name, expected",
    [
        ("2024-07-15 14:00", "Europe/Paris", ["2024-07-15 12:00"]),
        ("2024-01-15 14:00", "Europe/Paris", ["2024-01-15 13:00"]),
        ("2024-01-15 00:30", "Europe/Paris", ["2024-01-14 23:30"]),
        ("2024-07-15 14:00", "America/New_York", ["2024-07-15 18:00"]),
        ("2024-07-15 14:00", "Asia/Tokyo", ["2024-07-15 05:00"]),
        ("2024-07-15 14:00", "Asia/Kolkata", ["2024-07-15 08:30"]),
        ("2024-03-31 02:30", "Europe/Paris", None)

    ]
)

def test_convert_to_utc(start_time, timezone_name, expected):

    time_status, date_first, date_second = analyze_local_time(start_time, timezone_name)

    result = convert_to_utc(time_status, date_first, date_second, choice=None)

    assert result == expected
    


@pytest.mark.parametrize(
    "choice, expected",
    [
        ("1", ["2023-10-29 00:30"]),
        ("2", ["2023-10-29 01:30"]),
        ("3", ["2023-10-29 00:30", "2023-10-29 01:30"])
    ]
)

def test_convert_ambiguous_time(choice, expected):
    time_status, date_first, date_second = analyze_local_time(
        "2023-10-29 02:30", "Europe/Paris"
    )

    result = convert_to_utc(time_status, date_first, date_second, choice)
    assert result == expected