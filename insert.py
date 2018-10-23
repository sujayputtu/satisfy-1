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

    # This function is yet to be completed.
    def insert_user(self, *args):
        """Insert values into user table."""
        mail = args[0]
        fname = args[1]
        lname = args[2]
        passwd = args[3]
        dob = args[4]
        city = args[5]
        height = args[6]
        weight  = args[7]
        uid = 1
        age = 12

        sql = 'insert into user (uid, mail, Fname, Lname, passwd, dob, city, age, height, weight) values (%d, %s, %s, %s, %s, %s, %s, %d, %d, %d)'
        val = (uid, mail, fname, lname, passwd, dob, city, age, height, weight)

        self.cur.execute(sql, val)
        self.sat.commit()

    def insert_friend(self, *args):
        """Insert values into friend table."""
        pass

    def insert_run(self, *args):
        """Insert values into run table."""
        pass

    def insert_challenge(self, *args):
        """Insert values into challenge table."""
        pass