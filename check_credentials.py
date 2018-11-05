import mysql.connector as con

class credentials(object):
    def __init__(self):
        self.sat = con.connect(
            host = "localhost",
            user = "vadi",
            passwd = "Vadi@1998",
            database = "satisfy"
        )
        self.cur = self.sat.cursor()

    def login(self, mail, passwd):
        self.cur.execute('select uid from user_mail where mail = %s', mail)

        uid_t = self.cur.fetchone()
        uid = uid_t[0]

        self.cur.execute('select passwd from user where uid = %s', uid)

        obtain_t = self.cur.fetchone()
        obtain = obtain_t[0]

        if obtain == passwd:
            return True
        else:
            return False