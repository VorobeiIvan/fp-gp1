from datetime import datetime, timedelta
from collections import UserDict

class Record:
    """Represents a single record in the address book."""
    def __init__(self, name, birthday=None):
        self.name = name  # Name object with a 'value' attribute
        self.birthday = birthday  # Birthday object with a 'value' attribute


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