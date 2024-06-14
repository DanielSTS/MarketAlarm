import re


class Email:
    def __init__(self, email: str):
        if not re.match(r'^[\w.-]+@[\w.-]+$', email):
            raise ValueError("Invalid email address")
        self.value = email

    def __str__(self):
        return self.value
