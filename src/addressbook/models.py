from datetime import datetime
from collections import UserDict
import re


class Field:
    """Base class for fields in the address book."""
    def __init__(self, value):
        self.value = value


class Name(Field):
    """A class for storing the name field."""
    pass


class Birthday(Field):
    """A class for storing a birthday field."""
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)


class Phone(Field):
    """A class for storing and validating phone numbers."""
    def __init__(self, value):
        if not re.match(r"^\\+?\\d{10,15}$", value):
            raise ValueError("Invalid phone number format. Use digits with an optional '+' prefix.")
        super().__init__(value)


class Email(Field):
    """A class for storing and validating email addresses."""
    def __init__(self, value):
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", value):
            raise ValueError("Invalid email format.")
        super().__init__(value)


class Address(Field):
    """A class for storing addresses."""
    pass


class Record:
    """Represents a single record in the address book."""
    def __init__(self, name: Name, birthday: Birthday = None, phones=None, email=None, address=None):
        self.name = name
        self.birthday = birthday
        self.phones = phones if phones else []
        self.email = email
        self.address = address

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        self.phones = [p for p in self.phones if p.value != phone.value]

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def edit_email(self, new_email: Email):
        self.email = new_email

    def edit_address(self, new_address: Address):
        self.address = new_address


class AddressBook(UserDict):
    """Implementation of a basic address book."""

    def add_record(self, record: Record) -> None:
        """Add the record to the address book."""
        if record.name.value in self.data:
            raise KeyError(f"The record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        """Find the record by name."""
        return self.data.get(name)

    def delete(self, name: str) -> None:
        """Delete the record by name."""
        if name not in self.data:
            raise KeyError(f"The record with name '{name}' is not found.")
        del self.data[name]

    def edit_record(self, name: str, **kwargs):
        """Edit an existing record."""
        record = self.find(name)
        if not record:
            raise KeyError(f"The record with name '{name}' is not found.")
        if 'phones' in kwargs:
            record.phones = kwargs['phones']
        if 'email' in kwargs:
            record.edit_email(kwargs['email'])
        if 'address' in kwargs:
            record.edit_address(kwargs['address'])
        if 'birthday' in kwargs:
            record.birthday = kwargs['birthday']
