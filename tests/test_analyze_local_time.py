from dates_and_time import analyze_local_time
import pytest

# python -m pytest tests/test_analyze_local_time.py -v

@pytest.mark.parametrize(
    "start_time, timezone_name, expected_time_status, expected_date_first, expected_date_second",
    [
        ("2026-11-17 01:33", "Europe/Paris", "normal_time", "2026-11-17 01:33", None),
        ("2023-10-29 02:30", "Europe/Paris", "ambiguous_time", "2023-10-29 02:30", "2023-10-29 02:30"),
        ("2024-03-31 02:30", "Europe/Paris", "non_existent_time", None, None)
    ]
)

def test_analyze_local_time(start_time, timezone_name, expected_time_status, expected_date_first, expected_date_second):

    time_status, date_first, date_second = analyze_local_time(start_time, timezone_name)


    assert time_status == expected_time_status


    if expected_date_first is None:
        assert date_first is None
    else:
        assert date_first.strftime("%Y-%m-%d %H:%M") == expected_date_first
    
    
    if expected_date_second is None:
        assert date_second is None
    else:
        assert date_second.strftime("%Y-%m-%d %H:%M") == expected_date_second
        assert date_first.utcoffset() != date_second.utcoffset()