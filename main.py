from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from src.constants import COMMANDS, COMMAND_LIST
from src.contacts.contacts_manager import ContactsManager
from src.notes.notes_manager import NotesManager
from src.parser import parse_input
from src.decorators.colorize_message import print_error, print_success, print_warning
from src.commands import show_all, birthday_in_days

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
                        result = notes_manager.add_note()
                    case "show-notes":
                        result = notes_manager.list_notes()
                    case "search-notes":
                        result = notes_manager.search_notes()
                    case "delete-note":
                        result = notes_manager.delete_note()
                    case "edit-note":
                        result = notes_manager.edit_note()
                    case "sort-notes":
                        result = notes_manager.sort_notes_by_tag()

                    # General commands
                    case "show-all":
                        show_all()

                    case "birthday-in-days":
                        birthday_in_days()
                    case "birthdays":
                        birthday_in_days()
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
