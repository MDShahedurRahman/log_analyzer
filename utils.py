from utils import validate_date


def filter_by_level(entries, level):
    return [e for e in entries if e.level == level]


def filter_by_date(entries, date):
    if not validate_date(date):
        return []
    return [e for e in entries if e.date == date]
