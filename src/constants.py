from colorama import Fore

COMMANDS = {
    # General commands
    "show-all": "Show all contacts and notes.",
    "exit": "Exit the application.",
    "help": "Show available commands.",
    # Note-related commands
    "add-note": "This command allows you to add a new note.",
    "show-notes": "This command displays all saved notes.",
    "search-notes": "This command allows you to search notes by title, content, or tags.",
    "delete-note": "This command allows you to delete a note.",
    "edit-note": "This command allows you to edit a note.",
    "sort-notes": "Sort notes by tags length.",
    # Contact-related commands
    "add-contact": "Add a new contact.",
    "show-contacts": "Show all contacts.",
    "search-contacts": "Search for contacts by name or phone number.",
    "delete-contact": "Delete a contact.",
    "edit-contact": "Change an existing contact.",
    # Birthday-related commands
    "birthday-in-days": "Show contacts with birthdays in the next N days.",
}

CONTACTS_FIELDS = {
    "name": "Enter contact name (example: John Doe): ",
    "address": "Enter contact address (example: 123 Main St): ",
    "phone": "Enter contact phone number (example: +380121234567): ",
    "email": "Enter contact email (example: email@example.com): ",
    "birthday": "Enter contact birthday (example: 01-01-2000): "
    }

COMMAND_LIST = list(COMMANDS.keys())

group_ranges = {
    'General': (0, 3),
    'Notes': (3, 9),
    'Contacts': (9, 14),
    'Birthdays': (14, len(COMMANDS))
}

group_colors = {
    'General': Fore.CYAN,
    'Notes': Fore.MAGENTA,
    'Contacts': Fore.GREEN,
    'Birthdays': Fore.YELLOW,
}