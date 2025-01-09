from datetime import datetime
from src.contacts.contact_validators import (
    validate_name,
    validate_address,
    validate_phone,
    validate_email,
    validate_birthday
)
from src.storage import load_data, save_data
from src.decorators.handle_keyboard_interrupt import handle_keyboard_interrupt
from src.constants import CONTACTS_FIELDS
from src.decorators.colorize_message import print_error, print_success

class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday

    def __repr__(self):
        return f"Contact(name={self.name}, address={self.address}, phone={self.phone}, email={self.email}, birthday={self.birthday})"

class ContactsManager:
    def __init__(self, storage_file="contacts.pkl"):
        self.storage_file = storage_file
        self.contacts = load_data(self.storage_file)

    def save_contacts(self) -> None:
        save_data(self.contacts, self.storage_file)

    @handle_keyboard_interrupt
    def add_contact(self):
        contact = {}

        for field, prompt in CONTACTS_FIELDS.items():
            while True:
                value = input(prompt)
                if field == "name" and not validate_name(value, self.contacts):
                    continue
                elif field == "address" and not validate_address(value):
                    continue
                elif field == "phone" and not validate_phone(value):
                    continue
                elif field == "email" and not validate_email(value):
                    continue
                elif field == "birthday" and not validate_birthday(value):
                    continue
                contact[field] = value
                break

        contact_object = Contact(contact["name"], contact["address"], contact["phone"], contact["email"], contact["birthday"])
        self.contacts.append(contact_object)
        self.save_contacts()

        print_success(f"Contact '{contact['name']}' added successfully!")

    def show_contact(self, args):
        if len(args) == 0:
            return print_error("Please provide the name as an argument.")
        name = args[0]

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return print_error("Contact not found.")

    def show_all_contacts(self):
        if not self.contacts:
            return print_error("No contacts available.")
        return self.contacts

    def search_contacts(self, args):
        if len(args) == 0:
            return print_error("Please provide the keyword as an argument.")
        keyword = args[0]
        return [contact for contact in self.contacts if keyword.lower() in contact.name.lower()]

    def edit_contact(self, args):
        if len(args) == 0:
            return print_error("Please provide at least the index as an argument.")

        index = int(args[0])
        name = args[1] if len(args) > 1 else None
        address = args[2] if len(args) > 2 else None
        phone = args[3] if len(args) > 3 else None
        email = args[4] if len(args) > 4 else None
        birthday = args[5] if len(args) > 5 else None

        if index >= len(self.contacts):
            return print_error("Nothing found. Invalid index.")


        if name and not validate_name(name, self.contacts):
            return print_error("Name should not be empty.")
        if address and not validate_address(address):
            return print_error("Address is invalid. Please enter a valid address. Example: 123 Main St")
        if phone and not validate_phone(phone):
            return print_error("Phone number is invalid. Please enter a valid phone number. Example: +1234567890")
        if email and not validate_email(email):
            return print_error("Email is invalid. Please enter a valid email. Example: example@example.com")
        if birthday and not validate_birthday(birthday):
            return print_error("Birthday is invalid. Please enter a valid birthday. Example: 01-01-2000")

        contact = self.contacts[index]
        contact.name = name or contact.name
        contact.address = address or contact.address
        contact.phone = phone or contact.phone
        contact.email = email or contact.email
        contact.birthday = birthday or contact.birthday
        self.save_contacts()

    def delete_contact(self, args):
        if len(args) == 0:
            return print_error("Please provide the index as an argument.")
        index = int(args[0])

        if index >= len(self.contacts):
            return print_error("Nothing found. Invalid index.")
        del self.contacts[index]
        self.save_contacts()
        print_success(f"Contact deleted successfully!")

    def birthday_in_days(self, days):
        """
        Returns a list of contacts who have birthdays in the next 'days' days.
        """
        today = datetime.today()
        upcoming_contacts = []

        for contact in self.contacts:
            try:
                birthday = datetime.strptime(contact.birthday, "%d-%m-%Y")
                next_birthday = birthday.replace(year=today.year)

                # If the birthday has passed this year, check for the next year
                if next_birthday < today:
                    next_birthday = birthday.replace(year=today.year + 1)

                if 0 <= (next_birthday - today).days <= days:
                    upcoming_contacts.append(contact)
            except ValueError:
                print_error(f"Invalid birthday format for contact {contact.name}. Skipping...")

        return upcoming_contacts
