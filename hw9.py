USERS = {}

# decorator
def error_handler(func):
    def inner(*args):
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

def hello_user():
    return "Whats up"


def unknown_command(user_input):
    return f"unknown_command {user_input}"

def close_app():
    exit('Good Bye')

@error_handler
def add_user(name, phone):
    USERS[name] = phone
    return f'User {name} added!'

@error_handler
def change_phone(name: str, new_phone: str) -> str:
    if name in USERS:
        old_phone = USERS[name]
        USERS[name] = new_phone
        return f'User {name} has new number: {new_phone}, old phone number: {old_phone}'
    else:
        return f'This user: {name} is not in your phone book'


def show_all(*args) -> str:
    if not USERS:
        return 'No users in the phone book'
    result = ''
    for name, phone in USERS.items():
        result += f'Name: {name} phone: {phone}\n'
    return result

def show_phone(name:str) -> str:
    return f"{name}'s phone number is {USERS[name]}\n"

HANDLERS = {
    'hello': hello_user,
    'add': add_user,
    'change': change_phone,
    'phone': show_phone,
    'show all': show_all,
    'exit': close_app,
    'good bye': close_app,
    'close': close_app,
}

def parse_input(user_input):
    parts = user_input.split()
    user_input_name = parts[0]
    if user_input_name == 'show' and 'all' in parts:
        user_input_name = 'show all'
        user_input_args = []
    elif user_input_name == 'good' and 'bye' in parts:
        user_input_name = 'good bye'
        user_input_args = []
    elif len(parts)>1:
        user_input_args = parts[1:]
    else:
        user_input_args=[]
    return user_input_name, user_input_args

def main():
    print (hello_user())
    while True:
        # example: add Petro 0991234567
        user_input_line = input('Please enter command and args: ').strip().lower()
        user_input_name, user_input_args = parse_input(user_input_line)
        if user_input_name in HANDLERS:
            try:
                result = HANDLERS[user_input_name](*user_input_args)
                print(result)
            except TypeError:
                print('Invalid input')
        else:
            print(unknown_command(user_input_name))

if __name__ == '__main__':
    main()