from src.contacts.contact_validators import (
    validate_name,
    validate_address,
    validate_phone,
    validate_email,
    validate_birthday
)
from src.storage import load_data, save_data
from src.decorators.handle_keyboard_interrupt import handle_keyboard_interrupt
from src.decorators.colorize_message import print_success,print_warning
from src.constants import CONTACTS_FIELDS

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
    
        def safe_lower(value):
            return value.lower() if isinstance(value, str) else ""
    
        found_contacts = [contact for contact in self.contacts if 
                        query.lower() in safe_lower(contact.name) or
                        query.lower() in safe_lower(contact.address) or
                        query.lower() in safe_lower(contact.phone) or
                        query.lower() in safe_lower(contact.email) or
                        query.lower() in safe_lower(contact.birthday)]
    
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
        name = input("Enter the name of the contact to edit: ").strip()
        contact_to_edit = next((contact for contact in self.contacts if contact.name == name), None)

        if not contact_to_edit:
            print_warning(f"No contact found with the name '{name}'.")
            return

        print(f"Editing contact '{name}':")
        while True:
            new_address = input(f"Enter new address (current: {contact_to_edit.address}): ").strip() or contact_to_edit.address
            if validate_address(new_address):
                contact_to_edit.address = new_address
                break
            print("Invalid address. Please try again.")

        while True:
            new_phone = input(f"Enter new phone (current: {contact_to_edit.phone}): ").strip() or contact_to_edit.phone
            if validate_phone(new_phone):
                contact_to_edit.phone = new_phone
                break
            print("Invalid phone number. Please try again.")

        while True:
            new_email = input(f"Enter new email (current: {contact_to_edit.email}): ").strip() or contact_to_edit.email
            if validate_email(new_email):
                contact_to_edit.email = new_email
                break
            print("Invalid email address. Please try again.")

        while True:
            new_birthday = input(f"Enter new birthday (current: {contact_to_edit.birthday}): ").strip() or contact_to_edit.birthday
            if validate_birthday(new_birthday):
                contact_to_edit.birthday = new_birthday
                break
            print("Invalid birthday. Format should be DD-MM-YYYY.")

        self.save_contacts()
        print(f"Contact '{name}' updated successfully!")


