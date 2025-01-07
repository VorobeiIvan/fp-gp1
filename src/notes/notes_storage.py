import os
import pickle

from notes_models import NotesManager


class NotesStorage(NotesManager):
    """Клас для зберігання нотаток у файл з використанням pickle."""

    def load_notes(self):
        """Завантажити нотатки з файлу."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "rb") as file:
                return pickle.load(file)
        return {}

    def save_notes(self):
        """Зберегти нотатки у файл."""
        with open(self.storage_file, "wb") as file:
            pickle.dump(self.notes, file)
