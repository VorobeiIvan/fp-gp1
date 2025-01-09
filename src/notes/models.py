
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
