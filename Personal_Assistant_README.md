
# Personal Assistant

This project is a simple personal assistant that allows you to manage contacts and notes via the command line interface. Users can add, edit, delete, and view contacts and notes, along with several other features via the console.

## Project Overview

The Personal Assistant has the following features:
- Add, edit, delete, and view contacts.
- Add, edit, delete, and view notes.
- Search contacts and notes by various criteria.
- Command-line autocompletion support for user convenience.
- Styled output using the `colorama` library.

## Functionality

### Commands:
- **show-all** — Displays all contacts and notes.
- **add-contact** — Adds a new contact.
- **show-contact** — Displays a contact by name.
- **search-contacts** — Search contacts by name or phone number.
- **edit-contact** — Edit an existing contact.
- **delete-contact** — Delete a contact.
- **show-all-contacts** — Displays all contacts.
- **add-note** — Adds a new note.
- **show-notes** — Displays all notes.
- **search-notes** — Search notes by title, content, or tags.
- **delete-note** — Delete a note.
- **edit-note** — Edit a note.
- **exit** — Exit the application.
- **help** — Shows available commands.

### Requirements:
- Python 3.7+
- Libraries:
  - `prompt_toolkit~=3.0.48`
  - `colorama==0.4.6`

## How to Run

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/personal-assistant.git
```

### 2. Navigate to the project directory:
```bash
cd personal-assistant
```

### 3. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the program:
```bash
python main.py
```

### 5. Use the available commands in the command line.

## Project Structure

```bash
.
├── README.md               # Project description
├── contacts.pkl            # File for storing contacts
├── main.py                 # Main script to start the program
├── notes.pkl               # File for storing notes
├── requirements.txt        # List of dependencies
└── src
    ├── __pycache__         # Compiled Python files
    ├── constants.py        # Constants and commands
    ├── contacts            # Modules for managing contacts
    ├── decorators          # Decorators for styling and error handling
    ├── notes               # Modules for managing notes
    ├── parser.py           # Command parsing logic
    └── storage.py          # Module for data storage
```

## Contributing

Contributions to this project are welcome! To contribute, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.
