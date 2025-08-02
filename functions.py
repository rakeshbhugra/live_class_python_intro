from typing import Union

# Simple function
def print_hello_world():
    print("Hello, someoneg")
    print("Hello, Earth!")

print_hello_world()

# Function with arguments
def greet_user(name: str):
    print(f"Hello, {name}!")

greet_user("Alice")

# Function with arguments

def send_email(name: str, email: str) -> None:
    email_template = """Hello {name},
    Thank you for signing up for our service. We are excited to have you on board!
    Best regards,
    The Team
    """
    print(email_template.format(name=name))

    print("Email sent to:", email)

    return None


def add_numbers(a: int, b: int) -> int:
    return a + b

# example of multiple values returned by a function

def get_user_info():
    name = "Alice"
    age = 30
    email = "alice@example.com"
    return name, age, email

name, age, email = get_user_info()


print(f"Name: {name}, Age: {age}, Email: {email}")