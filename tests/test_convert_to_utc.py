import pytest
from dates_and_time import convert_to_utc


# python -m pytest tests/test_convert_to_utc.py -v


@pytest.mark.parametrize(
    "start_time, timezone_name, expected",
    [
        ("2024-07-15 14:00", "Europe/Paris", "2024-07-15 12:00"),
        ("2024-01-15 14:00", "Europe/Paris", "2024-01-15 13:00"),
        ("2024-01-15 00:30", "Europe/Paris", "2024-01-14 23:30"),
        ("2024-07-15 14:00", "America/New_York", "2024-07-15 18:00"),
        ("2024-07-15 14:00", "Asia/Tokyo", "2024-07-15 05:00"),
        ("2024-07-15 14:00", "Asia/Kolkata", "2024-07-15 08:30")
    ]
)
def test_convert_to_utc(start_time, timezone_name, expected):
    result = convert_to_utc(start_time, timezone_name)
    assert result == expected