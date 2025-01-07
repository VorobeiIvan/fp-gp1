import os
import pickle


class NotesManager:

    def __init__(self, storage_file="notes.pkl"):
        self.storage_file = storage_file
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "rb") as file:
                return pickle.load(file)
        return {}

    def save_notes(self):
        with open(self.storage_file, "wb") as file:
            pickle.dump(self.notes, file)

    def add_note(self):
        title = input("Enter note title: ")
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
