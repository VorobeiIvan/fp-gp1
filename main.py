from src.notes.models import NotesManager
from src.contacts.models import AddressBook, Record, Name, Birthday, Phone, Email, Address
from src.contacts.storage import get_upcoming_birthdays
from src.constants import COMMANDS, COMMAND_LIST
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter


def personal_assistant_app():
    notes_manager = NotesManager()
    address_book = AddressBook()

    commands_text = "\nAvailable commands:\n"
    for idx, (command, description) in enumerate(COMMANDS.items(), start=1):
        commands_text += f"{idx}. {command} - {description}\n"
    print(commands_text)

    command_completer = WordCompleter(COMMAND_LIST, ignore_case=True)
    session = PromptSession(completer=command_completer)

    while True:
        command = session.prompt("Enter a command: ").strip().lower()

        match command:
            case "add-note":
                notes_manager.add_note()

            case "show-notes":
                notes_manager.list_notes()

            case "add-contact":
                name = input("Enter name: ").strip()
                birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
                phone = input("Enter phone number (optional): ").strip()
                email = input("Enter email (optional): ").strip()
                address = input("Enter address (optional): ").strip()

                try:
                    record = Record(
                        name=Name(name),
                        birthday=Birthday(birthday) if birthday else None,
                        phones=[Phone(phone)] if phone else [],
                        email=Email(email) if email else None,
                        address=Address(address) if address else None,
                    )
                    address_book.add_record(record)
                    print(f"Contact '{name}' added successfully.")
                except ValueError as e:
                    print(f"Error: {e}")

            case "show-contacts":
                if not address_book.data:
                    print("Address book is empty.")
                else:
                    for name, record in address_book.data.items():
                        phones = ", ".join(phone.value for phone in record.phones)
                        print(
                            f"Name: {record.name.value}, "
                            f"Birthday: {record.birthday.value if record.birthday else 'N/A'}, "
                            f"Phones: {phones if phones else 'N/A'}, "
                            f"Email: {record.email.value if record.email else 'N/A'}, "
                            f"Address: {record.address.value if record.address else 'N/A'}"
                        )

            case "upcoming-birthdays":
                days = int(input("Enter number of days to check: ").strip())
                upcoming = get_upcoming_birthdays(address_book, days)
                if upcoming:
                    print("Upcoming birthdays:")
                    print(upcoming)
                else:
                    print("No upcoming birthdays.")

            case "exit":
                print("Exiting application. Goodbye!")
                break

            case _:
                print("Invalid command. Please try again.")
                print(commands_text)


if __name__ == "__main__":
    personal_assistant_app()
