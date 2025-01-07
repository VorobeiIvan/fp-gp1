from parser import parse_input

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

from commands import (add_birthday, add_contact, birthdays, change_contact,
                      exit_bot, show_all, show_birthday, show_phone, start_bot)
from constants import COMMAND_LIST, COMMANDS, messages, messages_error
from contacts.contacts_storage import load_data, save_data
from notes.notes_models import NotesManager


def personal_assistant_app():
    """Основний цикл бота."""
    contacts = load_data()  # Завантажуємо контактні дані
    print(messages["start_bot"])

    notes_manager = NotesManager()

    # Виведення доступних команд
    commands_text = "\nAvailable commands:\n"
    for idx, (command, description) in enumerate(COMMANDS.items(), start=1):
        commands_text += f"{idx}. {command} - {description}\n"
    print(commands_text)

    # Ініціалізація автодоповнення для команд
    command_completer = WordCompleter(COMMAND_LIST, ignore_case=True)
    session = PromptSession(completer=command_completer)

    while True:
        user_input = session.prompt(messages["user_input"])
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(contacts)
            print(exit_bot())
            break
        elif command == "hello":
            print(start_bot())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(args, contacts))
        elif command == "add-note":
            notes_manager.add_note()
        elif command == "show-notes":
            notes_manager.list_notes()
        elif command == "help":
            print(commands_text)
        else:
            print(messages_error["invalid"])
            print(commands_text)


if __name__ == "__main__":
    personal_assistant_app()
