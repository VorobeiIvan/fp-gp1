from datetime import datetime
from collections import UserDict


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


class Record:
    """Represents a single record in the address book."""
    def __init__(self, name: Name, birthday: Birthday = None):
        self.name = name
        self.birthday = birthday


class AddressBook(UserDict):
    """Implementation of basic version of the address book."""

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
