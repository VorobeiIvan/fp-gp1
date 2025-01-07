class Note:
    """Клас для представлення нотатки."""

    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []

    def __str__(self):
        tags_str = ", ".join(self.tags) if self.tags else "No tags"
        return f"Title: {self.title}\nContent: {self.content}\nTags: {tags_str}"


class NotesManager:
    """Клас для управління нотатками."""

    def __init__(self, storage_file="notes.pkl"):
        self.storage_file = storage_file
        self.notes = self.load_notes()

    def load_notes(self):
        """Завантажити нотатки з файлу."""
        raise NotImplementedError("Цей метод буде реалізовано в notes_storage.py")

    def save_notes(self):
        """Зберегти нотатки у файл."""
        raise NotImplementedError("Цей метод буде реалізовано в notes_storage.py")

    def add_note(self):
        """Додати нову нотатку."""
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        tags = (
            input("Enter tags (comma-separated): ").split(",")
            if input("Add tags? (y/n): ").strip().lower() == "y"
            else []
        )

        if title in self.notes:
            print("Note with this title already exists!")
            return

        self.notes[title] = Note(title, content, tags)
        self.save_notes()
        print(f"Note '{title}' added successfully!")

    def list_notes(self):
        """Переглянути всі нотатки."""
        if not self.notes:
            print("No notes available.")
        for note in self.notes.values():
            print(note)
