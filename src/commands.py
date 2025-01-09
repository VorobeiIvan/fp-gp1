from src.constants import messages, messages_error
from src.contacts.contacts_models import Birthday, Record
from src.decorators.colorize_message import colorize_message
from src.decorators.input_error import input_error


@colorize_message
@input_error
def add_contact(args, contacts):
    """Adds a contact to the dictionary."""
    if len(args) != 2:
        return messages_error["usage_add"]
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return messages["add_contact"]


@colorize_message
@input_error
def change_contact(args, contacts):
    """Changes the phone number for an existing contact."""
    if len(args) != 2:
        return messages_error["usage_change"]
    name, new_phone = args
    contact = contacts.find(name)
    if contact:
        contact.edit_phone(contact.phones[0].value, new_phone)
        return messages["change_contact"]
    return messages_error["not_found"]


@colorize_message
@input_error
def show_phone(args, contacts):
    """Returns the phone number by name."""
    if len(args) != 1:
        return messages_error["usage_phone"]
    name = args[0]
    contact = contacts.find(name)
    if contact:
        return contact.phones[0].value
    return messages_error["not_found"]


@colorize_message
@input_error
def show_all(contacts):
    """Displays all contacts."""
    if not contacts:
        return messages_error["no_contacts"]
    return "\n".join(str(record) for record in contacts.data.values())


@colorize_message
@input_error
def add_birthday(args, contacts):
    """Adds a birthday to a contact."""
    if len(args) != 2:
        return messages_error["usage_add_birthday"]
    name, birthday = args
    try:
        birthday_obj = Birthday(birthday)
    except ValueError:
        return messages_error["value_error"]
    contact = contacts.find(name)
    if contact:
        contact.add_birthday(birthday_obj)
        return f"Birthday for {name} added: {birthday_obj.value}"
    return messages_error["not_found"]


@colorize_message
@input_error
def show_birthday(args, contacts):
    """Shows the birthday for a contact."""
    if len(args) != 1:
        return messages_error["usage_show_birthday"]
    name = args[0]
    contact = contacts.find(name)
    if contact and contact.birthday:
        return f"{name}'s birthday is on {contact.birthday.value}"
    return messages_error["not_found"]


@colorize_message
@input_error
def birthdays(args, contacts):
    """Shows birthdays happening next week."""
    upcoming_birthdays = contacts.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No birthdays this week."
    return "\n".join(
        f"{contact.name}'s birthday is on {contact.birthday.value}"
        for contact in upcoming_birthdays
    )


@colorize_message
def start_bot():
    """Displays the start message."""
    return messages["start_message"]


@colorize_message
def exit_bot():
    """Displays the exit message."""
    return messages["exit_bot"]
