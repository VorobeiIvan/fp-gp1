from datetime import datetime, timedelta


def get_upcoming_birthdays(address_book):
    """Get upcoming birthdays within 7 days."""
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in address_book.values():
        if user.birthday:
            birthday_date = datetime.strptime(user.birthday.value, "%d.%m.%Y").date()
            birthday_this_year = birthday_date.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            days_until_birthday = (birthday_this_year - today).days

            if 0 <= days_until_birthday <= 7:
                if birthday_this_year.weekday() >= 5:
                    birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

                upcoming_birthdays.append(f"{user.name.value}: {birthday_this_year.strftime('%d.%m.%Y')}")

    return "\n".join(upcoming_birthdays)
