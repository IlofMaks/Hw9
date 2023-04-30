from typing import Dict

USERS: Dict[str,str] = {}
EXIT_FLAG = False

# decorator
def error_handler(func):
    def inner(args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "No user"
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner

def hello_user(_) -> str:
    return "How can I help you?"


def unknown_command(_) -> str:
    return "unknown_command"

def exit(_) -> None:
    global EXIT_FLAG
    EXIT_FLAG = True

@error_handler
def add_user(name, phone):
    USERS[name] = phone
    return f'User {name} added!'

@error_handler
def change_phone(name: str, phone: str) -> str:
    USERS[name] = phone
    return f'У {name} тепер телефон: {phone}'

def show_all(_) -> str:
    result = ''
    for name, phone in USERS.items():
        result += f'Name: {name} phone: {phone}\n'
    return result

def show_phone(name:str) -> str:
    phone = USERS.get(name)
    if phone is None:
        return "User not found"
    return f"{name}'s phone number is {phone}\n"

HANDLERS = {
    'hello': hello_user,
    'add': add_user,
    'change': change_phone,
    'phone': show_phone,
    'show all': show_all,
    'exit': exit,
    'goodbye': exit,
    'close': exit,
}

def parse_input(user_input):
    args = user_input.split()
    command = args[0].lower()

    if command == 'add':
        if len(args) != 3:
            return unknown_command, []
        name, phone = args[1:]
        return add_user, [name, phone]

    if command == 'change':
        if len(args) != 3:
            return unknown_command, []
        name, phone = args[1:]
        return change_phone, [name, phone]

    if command == 'phone':
        if len(args) != 2:
            return unknown_command, []
        name = args[1]
        return show_phone, name

    if command == 'show' and len(args) == 2 and args[1] == 'all':
        return show_all, []

    if command in ('hello', 'hi'):
        return hello_user, []

    if command in ('exit', 'quit', 'goodbye', 'close'):
        return exit, []

    return unknown_command, []


def main():
    while not EXIT_FLAG:
        # example: add Petro 0991234567
        user_input = input('Please enter command and args: ')
        handler, args = parse_input(user_input)
        result = handler(args)
        if not result:
            print('Good Bye')
            break
        print(result)

if __name__ == '__main__':
    main()