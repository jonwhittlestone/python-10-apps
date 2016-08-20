import datetime

def print_header():
    print('---------------------------')
    print('---------------------------')
    print('  WHEN IS YOUR BIRTHDAY!?  ')


def ask_for_birthday():
    day = input('What day is your birthday? ')
    month  = input('What month is your birthday? ')
    year = input('What year is your birthday? ')
    return datetime.datetime(int(year), int(month), int(day))


def compute_days_between_now_and_birthday(original_bday_date, now):
    # get birthday for this year
    bday_this_year = datetime.datetime(now.year, original_bday_date.month, original_bday_date.day)

    # calculate time delta
    dt = now - bday_this_year
    # convert to seconds
    days = int(dt.total_seconds() / 60 / 60 / 24)

    # return no. days
    return days


def print_output(days):
    if (days > 0):
        print('Your birthday was days {} ago' . format(-days))
    elif (days < 0):
        print('Your birthday is in {} days' . format(-days))
    else:
        print('Happy Birthday!')


def main():
    print_header()

    bday = ask_for_birthday()
    now = datetime.datetime.now()

    days = compute_days_between_now_and_birthday(bday, now)
    print_output(days)


main()
