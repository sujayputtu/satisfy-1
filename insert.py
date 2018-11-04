import mysql.connector as con
import datetime


class insert_val(object):
    """Function that inserts value into various tables."""
    def __init__(self):
        """Function that connects to the database."""
        self.sat = con.connect(
            host = "localhost",
            user = "vadi",
            passwd = "Vadi@1998",
            database = "satisfy"
        )
        self.cur = self.sat.cursor()

    def calculate_age(self, born):
        """To calculate age from date of birth."""
        today = datetime.date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def insert_user_mail (self, uid, mail):
        """Insert values into user_mail table."""
        pass

    def insert_user_age (self, uid, age):
        """Insert value into user_age table."""
        pass

    # This function is yet to be completed.
    def insert_user(self, *args):
        """Insert values into user table."""
        pass

    def insert_friend(self, *args):
        """Insert values into friend table."""
        pass

    def insert_run(self, *args):
        """Insert values into run table."""
        pass

    def insert_challenge(self, *args):
        """Insert values into challenge table."""
        pass