"""Leap year utility"""


def is_leap_year(year: int):
    """Calculated leap year."""
    if year%400 == 0 and year%100 == 0:
        return True
    elif year%4 == 0 and year%100 != 0:
        return True
    else:
        return False
        