def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    # Додавання нового контакту до словника
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid command."
    

def change_contact(args, contacts):
    # Змінює номер телефону для існуючого контакту
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."
    else:
        return "Invalid command."
    

def show_phone(args, contacts):
    # Показ номеру телефона для зазначеного контакту
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Invalid command."
    

def show_all(contacts):
    # Показує усі збережені контакти з номерами телефонів
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


