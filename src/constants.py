COMMANDS = {
    #General commands
    "hello": "Start the bot.",
    "exit": "Exit the application.",
    "close": "Exit the application.",
    "all": "Show all contacts.",
    "help": "Show available commands.",
    #Note commands
    "add-note": "This command allows you to add a new note.",
    "show-notes": "This command displays all saved notes.",
    "search-notes": "This command allows you to search notes by title, content, or tags.",
    "delete-note": "This command allows you to delete a note.",
    "edit-note": "This command allows you to edit a note.",
    #Contact commands
    "add-contact": "Add a new contact.",
    "change-contact": "Change an existing contact.",
    "phone": "Show the phone number by name.",
    #Birthday commands
    "add-birthday": "Add a birthday to a contact.",
    "show-birthday": "Show the birthday by name.",
    "birthdays": "Show birthdays happening next week.",
    
}


COMMAND_LIST = list(COMMANDS.keys())


messages_error = {
    "value_error": "Please provide both name and phone number.",
    "key_error": "Contact not found.",
    "index_error": "Please provide both name and phone number.",
    "type_error": "Invalid format. Please provide both name and phone number.",
    "invalid": "Invalid command. Please try again.",
    "not_found": "Contact not found.",
    "no_contacts": "No contacts found.",
    "usage_add": "Invalid input. Usage: add [name] [phone]",
    "usage_change": "Invalid input. Usage: change [name] [phone]",
    "usage_phone": "Invalid input. Usage: phone [name]",
    "usage_add_birthday": "Invalid input. Usage: add-birthday [name] [date]",
    "usage_show_birthday": "Invalid input. Usage: show-birthday [name]",
    "usage_birthdays": "Invalid input. Usage: birthdays",
}

messages = {
    "start_bot": "Welcome to the phone book bot!",
    "user_input": "Enter a command: ",
    "start_message": "How can I help you?",
    "add_contact": "Contact added.",
    "change_contact": "Contact updated.",
    "exit_bot": "Good bye!",
}
