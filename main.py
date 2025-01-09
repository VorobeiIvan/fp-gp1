from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from src.constants import COMMANDS, COMMAND_LIST
from src.contacts.contacts_manager import ContactsManager
from src.notes.notes_manager import NotesManager
from src.parser import parse_input
from src.decorators.colorize_message import print_error, print_success, print_warning, print_hint, print_default

def show_all():
    """Show all contacts and notes."""
    print_default("All contacts and notes:")
    print_hint("Contacts:")
    print_default(ContactsManager().show_all_contacts())
    print_hint("Notes:")
    print_default(NotesManager().list_notes())

def personal_assistant_app():
    """Main bot loop."""
    # Initialize ContactsManager and NotesManager for managing contacts and notes
    contacts_manager = ContactsManager()
    notes_manager = NotesManager()

    # Display the available commands to the user
    commands_text = "\nAvailable commands:\n"
    for idx, (command, description) in enumerate(COMMANDS.items(), start=1):
        commands_text += f"{idx}. {command} - {description}\n"
    print(commands_text)

    # Initialize command autocompletion to suggest commands as the user types
    command_completer = WordCompleter(COMMAND_LIST, ignore_case=True)
    session = PromptSession(completer=command_completer)

    while True:
        try:
            # Prompt the user to enter a command
            user_input = session.prompt("Enter a command: ")
            command, args = parse_input(user_input)
            result = None
            try:
                # Process the command
                match command:
                    # Contact-related commands
                    case "add-contact":
                        result = contacts_manager.add_contact()
                    case "show-contact":
                        result = contacts_manager.show_contact(args)
                    case "search-contacts":
                        result = contacts_manager.search_contacts(args)
                    case "delete-contact":
                        result = contacts_manager.delete_contact(args)
                    case "edit-contact":
                        result = contacts_manager.edit_contact(args)
                    case "show-all-contacts":
                        result = contacts_manager.show_all_contacts()

                    # Note-related commands
                    case "add-note":
                        result = notes_manager.add_note()
                    case "show-notes":
                        result = notes_manager.list_notes()
                    case "search-notes":
                        result = notes_manager.search_notes()
                    case "delete-note":
                        result = notes_manager.delete_note()
                    case "edit-note":
                        result = notes_manager.edit_note()

                    # General commands
                    case "show-all":
                        show_all()

                    case "birthday-in-days":
                        if not args:
                            print_error("Please provide the number of days as an argument.")
                            continue
                        try:
                            days = int(args[0])
                            contacts_with_upcoming_birthdays = contacts_manager.birthday_in_days(days)
                            if contacts_with_upcoming_birthdays:
                                print_success(f"Contacts with birthdays in the next {days} days:")
                                for contact in contacts_with_upcoming_birthdays:
                                    print(contact)
                            else:
                                print_error("No contacts with upcoming birthdays in the specified range.")
                        except ValueError:
                            print_error("Invalid input. Please provide a valid number of days.")

                    case "exit":
                        print_success("Exiting application. Goodbye!")
                        break

                    case "help":
                        result = commands_text

                    # Invalid command handler
                    case _:
                        result = print_warning("Invalid command. Please try again.")

                if result:
                    print(result)

            except Exception as e:
                print_error(f"Error occurred: {str(e)}")

        except KeyboardInterrupt:
            print_success("Exiting application. Goodbye!")
            break

if __name__ == "__main__":
    personal_assistant_app()