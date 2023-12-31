# a user with attached login info

from pwinput import pwinput


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # prompts the user for login credentials and returns a new User object with the same credentials
    @staticmethod
    def login_prompt(hidden: bool = True):
        new_username = input("Username: ")
        if hidden:
            new_password = pwinput(prompt="Password: ")
        else:
            new_password = input("Password: ")

        return User(new_username, new_password)
