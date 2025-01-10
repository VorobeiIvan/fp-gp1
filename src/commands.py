from src.contacts.contacts_manager import ContactsManager
from src.notes.notes_manager import NotesManager
from src.decorators.colorize_message import print_default, print_hint, print_success, print_warning, print_error
from datetime import datetime

def show_all():
    """Show all contacts and notes."""
    print_default("All contacts and notes:")
    print_hint("Contacts:")
    print_default(ContactsManager().show_contacts())
    print_hint("Notes:")
    print_default(NotesManager().list_notes())


def birthday_in_days():
    """
    Displays a list of contacts with their birthdays and the number of days until their next birthday.
    Allows the user to specify a range of days to filter the results.
    """
    try:
        days_range = input("Enter the number of days to filter birthdays (leave blank for all upcoming): ").strip()
        days_range = int(days_range) if days_range else None
    except ValueError:
        print_warning("Invalid input. Showing all upcoming birthdays.")
        days_range = None

    today = datetime.today()
    upcoming_contacts = []

    for contact in ContactsManager().contacts:
        if not contact.birthday:
            print_warning(f"Contact {contact.name} has no birthday information. Skipping...")
            continue

        try:
            # Parse the birthday
            birthday = datetime.strptime(contact.birthday, "%d-%m-%Y")
            next_birthday = birthday.replace(year=today.year)

            # Adjust for birthdays that have already passed this year
            if next_birthday < today:
                next_birthday = birthday.replace(year=today.year + 1)

            # Calculate the number of days until the next birthday
            days_until = (next_birthday - today).days

            # Filter based on the specified range if provided
            if days_range is None or days_until <= days_range:
                upcoming_contacts.append((contact.name, birthday.strftime("%d-%m-%Y"), days_until))
        except ValueError:
            print_error(f"Invalid birthday format for contact {contact.name}. Expected format is DD-MM-YYYY.")

    if upcoming_contacts:
        print_success("Upcoming birthdays:")
        for name, birthday, days_until in sorted(upcoming_contacts, key=lambda x: x[2]):
            print(f"- {name}: {birthday} (in {days_until} days)")
    else:
        print_warning("No contacts have valid birthday information or no birthdays within the specified range.")
