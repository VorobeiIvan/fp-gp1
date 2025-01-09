from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from src.constants import COMMANDS, COMMAND_LIST, messages, messages_error
from src.commands import (add_birthday, add_contact, birthdays, change_contact,
                      exit_bot, show_all, show_birthday, show_phone, start_bot)
from src.contacts.contacts_storage import load_data, save_data
from src.notes.models import NotesManager
from src.parser import parse_input


def personal_assistant_app():
    """Main bot loop."""
    contacts = load_data()  
    print(messages["start_bot"])
    notes_manager = NotesManager()

    # Displaying available commands
    commands_text = "\nAvailable commands:\n"
    for idx, (command, description) in enumerate(COMMANDS.items(), start=1):
        commands_text += f"{idx}. {command} - {description}\n"
    print(commands_text)

    # Initialization of command autocompletion
    command_completer = WordCompleter(COMMAND_LIST, ignore_case=True)
    session = PromptSession(completer=command_completer)

    while True:
        try:
            user_input = session.prompt(messages["user_input"])
            command, args = parse_input(user_input)

            match command:
                #Contact commands
                case "add-contact":
                    print(add_contact(args, contacts))

                case "change-contact":
                   print(change_contact(args, contacts))

                case "phone":
                    print(show_phone(args, contacts))

                
                #Birthday commands
                case "add-birthday":
                    print(add_birthday(args, contacts))

                case "show-birthday":
                    print(show_birthday(args, contacts))

                case "birthdays":
                    print(birthdays(args, contacts))

                #Note commands
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
                
                #General commands

                case "hello":
                    print(start_bot())

                case "exit"| "close":
                    save_data(contacts)
                    print(exit_bot())
                    break

                case "all":
                    print(show_all(contacts))

                case "help":
                    print(commands_text)

                case _:
                    print(messages_error["invalid"])
                    print(commands_text)
        except KeyboardInterrupt:
            print("Exiting application. Goodbye!")
            break


if __name__ == "__main__":
    personal_assistant_app()