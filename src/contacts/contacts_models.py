from collections import UserDict
from datetime import datetime, timedelta


# Базовий клас для полів запису
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Клас для зберігання імені контакту
class Name(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(value)


# Клас для зберігання номера телефону
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


# Клас для зберігання дня народження
class Birthday(Field):
    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError as exc:
            raise ValueError(
                "Невірний формат дати. Використовуйте формат DD.MM.YYYY"
            ) from exc
        super().__init__(self.value)


# Клас для зберігання інформації про контакт
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError(f"Phone number {phone} not found.")

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Phone number {old_phone} not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def __str__(self):
        phones = ", ".join([phone.value for phone in self.phones])
        birthday = self.birthday.value if self.birthday else "No birthday"
        return f"{self.name}: {phones}, Birthday: {birthday}"


# Клас для управління записами
class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError(f"Record with name {record.name.value} already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Record with name {name} not found.")

    def get_upcoming_birthdays(self):
        """Повертає список контактів, у яких день народження протягом наступного тижня."""
        today = datetime.today().date()
        next_week = today + timedelta(days=7)
        upcoming = []

        for record in self.data.values():
            if record.birthday:
                # Переносимо день народження на поточний рік
                birthday_this_year = record.birthday.value.replace(year=today.year)
                # Якщо день народження вже був цього року, переносимо на наступний рік
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                if today <= birthday_this_year <= next_week:
                    upcoming.append(record)

        return upcoming
