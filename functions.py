# def print_hello_world():
#     print("Hello, someoneg")
#     print("Hello, Earth!")


def send_email(name: str, email: str):
    email_template = """Hello {name},
    Thank you for signing up for our service. We are excited to have you on board!
    Best regards,
    The Team
    """
    print(email_template.format(name=name))

    print("Email sent to:", email)


