from src.contacts.contact_validators import (
    validate_name,
    validate_address,
    validate_phone,
    validate_email,
    validate_birthday
)
from src.storage import load_data, save_data
from src.decorators.handle_keyboard_interrupt import handle_keyboard_interrupt
from src.decorators.colorize_message import print_error,print_success,print_warning
from src.constants import CONTACTS_FIELDS
from datetime import datetime

class Contact:
    def __init__(self, name: str, address: str, phone: str, email: str, birthday: str):
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
        self.contacts = load_data(self.storage_file) or []

    def save_contacts(self) -> None:
        save_data(self.contacts, self.storage_file)

    @staticmethod
    def validate_name(name: str, contacts: list[Contact]) -> bool:
        if not name.strip():
            print_warning("Name should not be empty.")
            return False
        if any(contact.name == name for contact in contacts):
            print_warning("Contact with this name already exists!")
            return False
        return True


    @handle_keyboard_interrupt
    def add_contact(self) -> None:
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

    def show_contacts(self) -> None:
        if not self.contacts:
            print_warning("No contacts available.")
            return

        for contact in self.contacts:
            print_success(f"Name: {contact.name}\nAddress: {contact.address}\nPhone: {contact.phone}\nEmail: {contact.email}\nBirthday: {contact.birthday}\n")

    @handle_keyboard_interrupt
    def search_contacts(self) -> None:
        query = input("Enter search query: ")
        found_contacts = [contact for contact in self.contacts if 
                          query.lower() in contact.name.lower() or
                          query.lower() in contact.address.lower() or
                          query.lower() in contact.phone.lower() or
                          query.lower() in contact.email.lower() or
                          query.lower() in contact.birthday.lower()]

        if not found_contacts:
            print_warning(f"No contacts found for '{query}'.")
        else:
            for contact in found_contacts:
                print_success(f"Name: {contact.name}\nAddress: {contact.address}\nPhone: {contact.phone}\nEmail: {contact.email}\nBirthday: {contact.birthday}\n")

    @handle_keyboard_interrupt
    def delete_contact(self) -> None:
        name = input("Enter the name of the contact to delete: ")
        contact_to_delete = next((contact for contact in self.contacts if contact.name == name), None)

        if not contact_to_delete:
            print_warning(f"No contact found with the name '{name}'.")
            return

        confirmation = input(f"Are you sure you want to delete the contact '{name}'? (y/n): ").strip().lower()
        if confirmation != 'y':
            print_warning("Contact deletion cancelled.")
            return

        self.contacts.remove(contact_to_delete)
        self.save_contacts()
        print_success(f"Contact '{name}' deleted successfully!")

    @handle_keyboard_interrupt
    def edit_contact(self) -> None:
        name = input("Enter the name of the contact to edit: ")
        contact_to_edit = next((contact for contact in self.contacts if contact.name == name), None)

        if not contact_to_edit:
            print_warning(f"No contact found with the name '{name}'.")
            return

        new_address = input(f"Enter new address (current: {contact_to_edit.address}): ").strip() or contact_to_edit.address
        new_phone = input(f"Enter new phone (current: {contact_to_edit.phone}): ").strip() or contact_to_edit.phone
        new_email = input(f"Enter new email (current: {contact_to_edit.email}): ").strip() or contact_to_edit.email
        new_birthday = input(f"Enter new birthday (current: {contact_to_edit.birthday}): ").strip() or contact_to_edit.birthday

        contact_to_edit.address = new_address
        contact_to_edit.phone = new_phone
        contact_to_edit.email = new_email
        contact_to_edit.birthday = new_birthday

        self.save_contacts()
        print_success(f"Contact '{name}' updated successfully!")

    @handle_keyboard_interrupt
    def birthday_in_days(self, days: int) -> None:
        today = datetime.today()
        birthday_contacts = []
        for contact in self.contacts:
            try:
                birthday = datetime.strptime(contact.birthday, "%d-%m-%Y")
                birthday = birthday.replace(year=today.year)
                if birthday < today:
                    birthday = birthday.replace(year=today.year + 1)
                if 0 <= (birthday - today).days <= days:
                    birthday_contacts.append(contact)
            except ValueError:
                print_error(f"Invalid birthday format for contact {contact.name}: {contact.birthday}")

        if birthday_contacts:
            for contact in birthday_contacts:
                print_success(f"Upcoming birthday: {contact}")
        else:
            print_warning("No upcoming birthdays found.")
