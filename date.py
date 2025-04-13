import datetime


def dates_are_same_of_year(a: datetime.date, b: datetime.date) -> bool:
    same_month = a.month == b.month
    same_day = a.day == b.day
    return same_month and same_day
