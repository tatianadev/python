from calendar import setfirstweekday, day_name, month_name, monthrange, MONDAY
from datetime import date
from time import strptime

setfirstweekday(MONDAY)

number_of_day = None
min_year = 1970
current_date = str(date.today())
print("Current date: %s" % current_date)

# parsed date value
parsed_date = strptime(current_date, '%Y-%m-%d')
start_year = parsed_date.tm_year
start_month = parsed_date.tm_mon


def find_year_and_month(input_start_year, input_start_month, input_min_year, input_number_of_day):
    while input_start_year > input_min_year:
        # monthrange returns weekday of first day of the month and number of days in month.
        if monthrange(input_start_year, input_start_month)[0] == input_number_of_day:
            final_year = input_start_year
            final_month = input_start_month
            return final_year, final_month
        else:
            if input_start_month > 1:
                input_start_month -= 1
            else:
                input_start_year -= 1
                input_start_month = 12


# input value
input_value = input('Enter day of week: ')

names_of_days = list(day_name)

if input_value not in names_of_days:
    print("Not existing name of day!")
    print("Possible values:")
    for a in names_of_days:
        print("%s" % a)
else:
    for i in range(len(names_of_days)):
        if input_value == names_of_days[i]:
            number_of_day = i
            print("Number of day: %d" % number_of_day)
            result_data = find_year_and_month(start_year, start_month, min_year, number_of_day)
            print("Year: %d, month: %d(%s)" % (result_data[0], result_data[1], month_name[result_data[1]]))
