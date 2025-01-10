import re
from datetime import datetime
from src.decorators.colorize_message import print_error, print_warning


def validate_name(name: str, contacts) -> bool:
    if not name.strip():
        print_warning("Name should not be empty.")
        return False
    if any(contact.name == name for contact in contacts):
        print_warning("Contact with this Name already exists!")
        return False
    return True


def validate_address(address) -> bool:
    if not address.strip():
        print_warning("Address should not be empty.")
        return False
    pattern = r'^[a-zA-Z0-9\s,.-]{10,}$'
    if not re.match(pattern, address):
        print_error("Address is invalid. Please enter a valid address. Example: 123 Main St")
        return False
    return True


def validate_phone(phone) -> bool:
    pattern = r'^\+?\d{1,3}?\d{10}$'
    if not re.match(pattern, phone):
        print_error("Phone number is invalid. Please enter a valid phone number. Example: +1234567890")
        return False
    return True


def validate_email(email) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email):
        print_error("Email is invalid. Please enter a valid email. Example: example@example.com")
        return False
    return True


def validate_birthday(birthday) -> bool:
    date_formats = ["%d-%m-%Y"]
    for date_format in date_formats:
        try:
            datetime.strptime(birthday, date_format)
            return True
        except ValueError:
            continue
    print_error("Birthday is invalid. Please enter a valid birthday. Example: 01-01-2000")
    return False

