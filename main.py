from src.notes.models import NotesManager


def personal_assistant_app():
    notes_manager = NotesManager()

    commands = """
Available commands:
1. add-note - Add a new note
2. show-notes - Show all notes
3. exit - Exit the application
    """

    print(commands)

    while True:
        command = input("Enter a command: ").strip().lower()

        match command:
            case "add-note":
                notes_manager.add_note()

            case "show-notes":
                notes_manager.list_notes()

            case "exit":
                print("Exiting application. Goodbye!")
                break

            case _:
                print("Invalid command. Please try again.")
                print(commands)


if __name__ == "__main__":
    personal_assistant_app()
