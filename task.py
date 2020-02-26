def firstrun():
    return "success"


def cir_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


def first_y_last(lost):
    return lost[0], lost[-1]


def date_between(date1, date2):
    delta = date2 - date1
    return delta.days
