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

    def get_uid(self):
        """Generate uid for new users."""
        with open("uid.txt", "r+") as uid_file:
            uid = int(uid_file.read())
            uid += 1
            uid_file.write(uid)
            
        return uid

    def calculate_age(self, born):
        """To calculate age from date of birth."""
        today = datetime.date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def insert_user_mail (self, uid, mail):
        """Insert values into user_mail table."""
        sql = 'insert into user_mail (uid, mail) values (%s, %s)'
        val = (uid, mail)

        self.cur.execute(sql, val)

    def insert_user_age (self, uid, age):
        """Insert value into user_age table."""
        sql = 'insert into user_age (uid, age) values (%s, %s)'
        val = (uid, age)

        self.cur.execute(sql, val)

    # This function is yet to be completed.
    def insert_user(self, *args):
        """Insert values into user table."""
        uid = self.get_uid()

        sql = 'insert into user (uid, fname, lname, passwd, dob, city, height, weight, tot_dist, tot_time) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (uid, args[1], args[2], args[3], args[4], args[5], args[6], args[7], 0.0, 0.0)

        self.cur.execute(sql, val)

        self.insert_user_mail(uid, args[0])
        
        age = self.calculate_age(args[4])
        self.insert_user_age(uid, age)

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