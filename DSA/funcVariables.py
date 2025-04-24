from datetime import datetime

@lambda _: _()
def get_current_time():
    """Returns the current time in HH:MM:SS format."""
    return datetime.now().strftime("%H:%M:%S")


print(get_current_time)