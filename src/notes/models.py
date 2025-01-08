import os
import pickle


class NotesManager:

    def __init__(self, storage_file="notes.pkl"):
        self.storage_file = storage_file
        self.notes = self.load_notes()

    def validate_title(self, title: str) -> bool:
        if not title.strip():
            print("Title should not be empty.")
            return False
        if title in self.notes:
            print("Note with this title already exists!")
            return False
        return True

    def load_notes(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "rb") as file:
                return pickle.load(file)
        return {}

    def save_notes(self) -> None:
        with open(self.storage_file, "wb") as file:
            pickle.dump(self.notes, file)

    def add_note(self):
        try:
            title = input("Enter note title: ")
            if not self.validate_title(title):
                return self.add_note()

            content = input("Enter note content: ")
            tags = input("Enter tags (comma-separated): ").split(",") if input(
                "Add tags? (y/n): ").strip().lower() == "y" else []

            if title in self.notes:
                print("Note with this title already exists!")
                return

            self.notes[title] = {
                "content": content,
                "tags": tags if tags else []
            }
            self.save_notes()
            print(f"Note '{title}' added successfully!")

        except KeyboardInterrupt:
            print("\nOperation cancelled. Returning to main menu.")

    def list_notes(self):
        if not self.notes:
            print("No notes available.")
        for title, note in self.notes.items():
            print(f"Title: {title}\nContent: {note['content']}\nTags: {', '.join(note['tags'])}\n")

    def search_notes(self):
        try:
            query = input("Enter search query: ")
            found_notes = {title: note for title, note in self.notes.items() if
                           query.lower() in title.lower() or
                           query.lower() in note['content'].lower() or
                           any(query.lower() in tag.lower() for tag in note['tags'])}

            if not found_notes:
                print(f"No notes found for '{query}'.")
            else:
                for title, note in found_notes.items():
                    print(f"Title: {title}\nContent: {note['content']}\nTags: {', '.join(note['tags'])}\n")

        except KeyboardInterrupt:
            print("\nOperation cancelled. Returning to main menu.")

    def delete_note(self):
        try:
            title = input("Enter the title of the note to delete: ")
            if title not in self.notes:
                print(f"No note found with the title '{title}'.")
                return

            confirmation = input(f"Are you sure you want to delete the note '{title}'? (y/n): ").strip().lower()
            if confirmation != 'y':
                print("Note deletion cancelled.")
                return

            del self.notes[title]
            self.save_notes()
            print(f"Note '{title}' deleted successfully!")

        except KeyboardInterrupt:
            print("\nOperation cancelled. Returning to main menu.")