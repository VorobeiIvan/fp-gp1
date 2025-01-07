COMMANDS = {
    "add-note": "Add a new note.",
    "show-notes": "Displays all saved notes.",
    "exit": "Exit the application.",
    "close": "Exit the application.",
    "hello": "Displays a greeting message.",
    "add": "Add a new contact.",
    "change": "Change the phone number of an existing contact.",
    "phone": "Displays the phone number of a contact.",
    "all": "Displays all contacts.",
    "add-birthday": "Add a birthday to a contact.",
    "show-birthday": "Displays the birthday of a contact.",
    "birthdays": "Displays all birthdays.",
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
