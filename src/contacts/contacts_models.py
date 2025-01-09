from collections import UserDict
from datetime import datetime, timedelta


# Base class for record fields
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Class for storing a contact's name
class Name(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(value)


# Class for storing a phone number
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


# Class for storing a birthday
class Birthday(Field):
    def __init__(self, value: str):
        try:
            # Parse the date in DD.MM.YYYY format
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError as exc:
            raise ValueError(
                "Invalid date format. Use the format DD.MM.YYYY"
            ) from exc
        super().__init__(self.value)


# Class for storing contact information
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        """Adds a phone number to the contact."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """Removes a phone number from the contact."""
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError(f"Phone number {phone} not found.")

    def edit_phone(self, old_phone, new_phone):
        """Edits an existing phone number."""
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Phone number {old_phone} not found.")

    def find_phone(self, phone):
        """Finds a specific phone number."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday: Birthday):
        """Adds a birthday to the contact."""
        self.birthday = birthday

    def __str__(self):
        """Returns a string representation of the contact."""
        phones = ", ".join([phone.value for phone in self.phones])
        birthday = self.birthday.value if self.birthday else "No birthday"
        return f"{self.name}: {phones}, Birthday: {birthday}"


# Class for managing contact records
class AddressBook(UserDict):
    def add_record(self, record):
        """Adds a record to the address book."""
        if record.name.value in self.data:
            raise ValueError(f"Record with name {record.name.value} already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        """Finds a record by name."""
        return self.data.get(name)

    def delete(self, name):
        """Deletes a record by name."""
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Record with name {name} not found.")

    def get_upcoming_birthdays(self):
        """Returns a list of contacts with birthdays in the next week."""
        today = datetime.today().date()
        next_week = today + timedelta(days=7)
        upcoming = []

        for record in self.data.values():
            if record.birthday:
                # Adjust the birthday to the current year
                birthday_this_year = record.birthday.value.replace(year=today.year)
                # If the birthday has already passed this year, adjust to next year
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                if today <= birthday_this_year <= next_week:
                    upcoming.append(record)

        return upcoming
