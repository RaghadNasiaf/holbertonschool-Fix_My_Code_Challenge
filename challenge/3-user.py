#!/usr/bin/python3
"""
User class
"""
import hashlib


class User:
    """
    User class
    """
    def __init__(self):
        self.password = ""

    def set_password(self, pwd):
        """
        set password
        """
        if pwd is None:
            self.password = None
        else:
            self.password = hashlib.md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        """
        validate password
        """
        if self.password is None or pwd is None:
            return False
        return self.password == hashlib.md5(pwd.encode()).hexdigest()
