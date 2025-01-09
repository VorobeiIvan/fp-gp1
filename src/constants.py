COMMANDS = {
    "show-all": "Show all contacts and notes.",
    "exit": "Exit the application.",
    "help": "Show available commands.",
    "add-note": "This command allows you to add a new note.",
    "show-notes": "This command displays all saved notes.",
    "search-notes": "This command allows you to search notes by title, content, or tags.",
    "delete-note": "This command allows you to delete a note.",
    "edit-note": "This command allows you to edit a note.",
    "add-contact": "Add a new contact.",
    "show-contact": "Show the phone number by name.",
    "search-contacts": "Search for contacts by name or phone number.",
    "edit-contact": "Change an existing contact.",
    "sort-notes": "Sort notes by tags length.",
    "delete-contact": "Delete a contact.",
    "show-all-contacts": "Show all contacts.",
    "birthday-in-days": "Show contacts with birthdays in the next N days."
}

CONTACTS_FIELDS = {
        "name": "Enter contact name (example: John Doe): ",
        "address": "Enter contact address (example: 123 Main St): ",
        "phone": "Enter contact phone number (example: +380121234567): ",
        "email": "Enter contact email (example: email@example.com): ",
        "birthday": "Enter contact birthday (example: 01-01-2000): "
        }

COMMAND_LIST = list(COMMANDS.keys())
