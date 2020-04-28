# 4.4
################


def gen_secs():
    secs = 0
    while secs < 60:
        yield secs
        secs += 1


def gen_minutes():
    minutes = 0
    while minutes < 60:
        yield minutes
        minutes += 1


def gen_hours():
    hours = 0
    while hours < 24:
        yield hours
        hours += 1


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2019):
    year = start
    while year < 2020:
        yield year
        year += 1


def gen_months():
    month = 1
    while month < 13:
        yield month
        month += 1


def gen_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        for day in range(1, 32):
            yield day
    elif month in [4, 6, 9, 11]:
        for day in range(1, 31):
            yield day
    elif month == 2:
        if leap_year:
            for day in range(1, 30):
                yield day
        else:
            for day in range(1, 29):
                yield day


def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, leap_year(year)):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


if __name__ == "__main__":
    # for gt in gen_time():
    #     print(gt)
    for date in gen_date():
        print(date)
