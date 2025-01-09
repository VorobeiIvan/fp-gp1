import os
import pickle
from src.decorators.handle_keyboard_interrupt import handle_keyboard_interrupt


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

    @handle_keyboard_interrupt
    def add_note(self):

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

    def list_notes(self):
        if not self.notes:
            print("No notes available.")
        for title, note in self.notes.items():
            print(f"Title: {title}\nContent: {note['content']}\nTags: {', '.join(note['tags'])}\n")

    @handle_keyboard_interrupt
    def search_notes(self):

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

    @handle_keyboard_interrupt
    def delete_note(self):

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

    @handle_keyboard_interrupt
    def edit_note(self):

        title = input("Enter the title of the note to edit: ")
        if title not in self.notes:
            print(f"No note found with the title '{title}'.")
            return

        print(f"Current content: {self.notes[title]['content']}")
        print(
            f"Current tags: {', '.join(self.notes[title]['tags']) if self.notes[title]['tags'] else 'No tags'}")

        confirmation = input(f"Do you want to edit the note '{title}'? (y/n): ").strip().lower()
        if confirmation != 'y':
            print("Note editing cancelled.")
            return

        new_content = input("Enter new content for the note (leave empty to keep current): ").strip()
        new_tags = input("Enter new tags (comma-separated, leave empty to keep current): ").strip()

        if new_content:
            self.notes[title]['content'] = new_content
        if new_tags:
            self.notes[title]['tags'] = [tag.strip() for tag in new_tags.split(",") if tag.strip()]

        self.save_notes()

        print(f"Note '{title}' updated successfully!")
