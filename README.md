# Personal Assistant

This project is a simple personal assistant that allows you to manage contacts and notes via the command line interface. Users can add, edit, delete, and view contacts and notes, along with several other features via the console.

## Project Overview

The Personal Assistant has the following features:

- Add, edit, delete, and view contacts.
- Add, edit, delete, and view notes.
- Search contacts and notes by various criteria.
- Command-line autocompletion support for user convenience.
- Styled output using the `colorama` library.
- Sort notes by tag length.
- Display upcoming birthdays within a specified number of days.

## Functionality

### Commands:

- `show-all` — Displays all contacts and notes.
- `add-contact` — Adds a new contact.
- `show-contact` — Displays a contact by name.
- `search-contacts` — Searches contacts by name or phone number.
- `edit-contact` — Edits an existing contact.
- `delete-contact` — Deletes a contact.
- `show-all-contacts` — Displays all contacts.
- `add-note` — Adds a new note.
- `show-notes` — Displays all notes.
- `search-notes` — Searches notes by title, content, or tags.
- `delete-note` — Deletes a note.
- `edit-note` — Edits a note.
- `sort_note` — Sorts notes by the length of their tags.
- `birthday-in-days` — Displays contacts with birthdays in the next N days.
- `exit` — Exits the application.
- `help` — Shows available commands.

### Requirements:

- Python 3.7+

### Required Libraries:

- `prompt_toolkit~=3.0.48`
- `colorama==0.4.6`

## How to Run

1. Clone the Repository:

   ```bash
   git clone https://github.com/VorobeiIvan/fp-gp1.git
   ```

2. Navigate to the Project Directory:

   ```bash
   cd personal-assistant
   ```

3. Set Up a Virtual Environment:

   - For Windows:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

   - For macOS/Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the Program:

   ```bash
   python3 main.py
   ```

## Usage Notes

- Use the `help` command to view the list of all available commands and their usage.
- Ensure that the `requirements.txt` file is up-to-date with the correct versions of dependencies.
- Keep your Python version compatible with the specified requirements to avoid runtime issues.
