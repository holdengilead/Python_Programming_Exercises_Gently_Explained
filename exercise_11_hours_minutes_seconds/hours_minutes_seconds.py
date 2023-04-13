def get_hours_minutes_seconds(total_seconds: int) -> str:
    seconds = total_seconds % 60
    time = ""
    if hours := total_seconds // 3600:
        time += f"{hours}h "
    if minutes := (total_seconds - 3600 * hours) // 60:
        time += f"{minutes}m "
    if seconds or not time:
        time += f"{seconds}s"
    return time.rstrip()


if __name__ == "__main__":
    assert get_hours_minutes_seconds(30) == "30s"
    assert get_hours_minutes_seconds(60) == "1m"
    assert get_hours_minutes_seconds(90) == "1m 30s"
    assert get_hours_minutes_seconds(3600) == "1h"
    assert get_hours_minutes_seconds(3601) == "1h 1s"
    assert get_hours_minutes_seconds(3661) == "1h 1m 1s"
    assert get_hours_minutes_seconds(90042) == "25h 42s"
    assert get_hours_minutes_seconds(0) == "0s"
