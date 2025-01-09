from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from src.constants import COMMANDS, COMMAND_LIST
from src.contacts.contacts_manager import ContactsManager
from src.notes.notes_manager import NotesManager
from src.parser import parse_input
from src.decorators.colorize_message import print_error, print_success, print_warning, print_hint

def show_all():
    """Show all contacts and notes."""
    print_hint("All contacts and notes:")
    print_hint("Contacts:")
    ContactsManager().show_contacts()
    print_hint("Notes:")
    NotesManager().list_notes()

def personal_assistant_app():
    """Main bot loop."""
    # Initialize managers
    contacts_manager = ContactsManager()
    notes_manager = NotesManager()

    # Display available commands
    commands_text = "\nAvailable commands:\n"
    for idx, (command, description) in enumerate(COMMANDS.items(), start=1):
        commands_text += f"{idx}. {command} - {description}\n"
    print_hint(commands_text)

    # Initialize autocompletion
    command_completer = WordCompleter(COMMAND_LIST, ignore_case=True)
    session = PromptSession(completer=command_completer)

    while True:
        try:
            # Get user input
            user_input = session.prompt("Enter a command: ")
            command, args = parse_input(user_input)

            # Command processing
            match command:
                # Contact-related commands
                case "add-contact":
                    contacts_manager.add_contact()
                case "show-contacts":
                    contacts_manager.show_contacts()
                case "search-contacts":
                    contacts_manager.search_contacts()
                case "delete-contact":
                    contacts_manager.delete_contact()
                case "edit-contact":
                    contacts_manager.edit_contact()

                # Note-related commands
                case "add-note":
                    notes_manager.add_note()
                case "show-notes":
                    notes_manager.list_notes()
                case "search-notes":
                    notes_manager.search_notes()
                case "delete-note":
                    notes_manager.delete_note()
                case "edit-note":
                    notes_manager.edit_note()

                # Birthday-related commands
                case "birthday-in-days":
                    contacts_manager.birthday_in_days()

                # General commands
                case "show-all":
                    show_all()
                case "exit":
                    print_success("Exiting application. Goodbye!")
                    break
                case "help":
                    print_hint(commands_text)

                # Invalid command
                case _:
                    print_warning("Invalid command. Please try again.")

        except Exception as e:
            print_error(f"Error occurred: {str(e)}")
        except KeyboardInterrupt:
            print_success("Exiting application. Goodbye!")
            break

if __name__ == "__main__":
    personal_assistant_app()
