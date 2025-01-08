from src.constants import COMMANDS, COMMAND_LIST
from src.notes.models import NotesManager
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter


def personal_assistant_app():
    notes_manager = NotesManager()

    commands_text = "\nAvailable commands:\n"
    for idx, (command, description) in enumerate(COMMANDS.items(), start=1):
        commands_text += f"{idx}. {command} - {description}\n"
    print(commands_text)

    command_completer = WordCompleter(COMMAND_LIST, ignore_case=True)
    session = PromptSession(completer=command_completer)

    while True:
        try:
            command = session.prompt("Enter a command: ").strip().lower()

            match command:
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

                case "exit":
                    print("Exiting application. Goodbye!")
                    break

                case _:
                    print("Invalid command. Please try again.")
                    print(commands_text)
        except KeyboardInterrupt:
            print("Exiting application. Goodbye!")
            break


if __name__ == "__main__":
    personal_assistant_app()
