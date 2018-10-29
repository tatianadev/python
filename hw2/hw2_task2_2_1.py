from calendar import weekday, day_name
from time import strptime


def find_day_of_week(input_value):
    # strptime() parses a string representing a time according to provided format
    valid_date = strptime(input_value, '%d.%m.%Y')

    input_year = valid_date.tm_year
    input_month = valid_date.tm_mon
    input_day = valid_date.tm_mday

    # find number of day of the week
    number_of_day = weekday(input_year, input_month, input_day)

    # find name of day of the week by value
    name_of_day = list(day_name)[number_of_day]  # list(day_name) - лишняя операция, просто day_name[number_of_day]
    return name_of_day


# input value
input_date = input("Enter date of your birth(in format DD.MM.YYYY): ")
found_name_of_day = find_day_of_week(input_date)

print("%s" % found_name_of_day)
