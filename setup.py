"""
This script has the necessary instructions to create all the tables requires.

This script has to be run only once, because it does nothing but creation of the tables.
"""

import mysql.connector as con

"""
The following segment contains information required to login to the database.

'host' will address the server where the database is present (In this case 'localhost').
'user' will be the user name for the database login.
'passwd' will be the password associated to the 'user'.
'database' will be the database name under the 'user'.
"""
satisfy = con.connect (
    host = "localhost",
    user = "vadi",
    passwd = "Vadi@1998",
    database = "satisfy"
)

# Creating cursor to use MySQL commands
cur = satisfy.cursor()

# Creating 'user' table
'''
    uid int; not null; primary key
    mail varchar(30); not null
    Fname varchar(20); not null
    Lname varchar(20); not null
    DOB date; not null
    passwd varcahr(30); not null
    city varchar(20); not null
    age int;
    height int;
    weight int;
'''
cur.execute('create table user (uid int primary key, mail varchar(30) not null, Fname varchar(20) not null, Lname varchar(20) not null, passwd varchar(30) not null, dob date not null, city varchar(20) not null, age int, height int, weight int)')

# Creating 'friend' table
'''
    uid int; not null; foreign key
    fid int; not null; foreign key

    uid & fid :- primary key
'''
cur.execute('create table friend (uid int not null, fid int not null, primary key (uid, fid), constraint friend_fk foreign key(uid) references user(uid) on delete cascade)')

# Creating'run' table
'''
    uid int; not null; foreign key
    distance int; not null
    type varchar(10); not null
    time int; not null
    speed int; not null
    bpm int;
    calories int
    elevation int

    distance & type & time :- primary key
'''
cur.execute('create table run (uid int not null, distance int not null, type varchar(10) not null, time int not null, speed int not null, calories int not null, bpm int, elevation int, constraint run_fk foreign key(uid) references user(uid), primary key(distance, type, time))')

# Creating 'challenge' table
'''
    cid int; not null; primary key
    distance int; not null; foreign key
    type varchar(10); not null; foreign key
    time int; not null; foreign key
    uid int; not null; foreign key
'''
cur.execute('create table challenge (cid int auto_increment primary key, distance int not null, type varchar(10) not null, time int not null, uid int not null, constraint chal1_fk foreign key(distance, type, time) references run(distance, type, time) on delete cascade, constraint chal2_fk foreign key(uid) references user(uid))')

# Creating 'participate' table
'''
    cid int; not null; foreign key
    uid int; not null; foreign key

    cid & uid :- primary key
'''
cur.execute('create table participate (cid int not null, uid int not null, constraint part1_fk foreign key(cid) references challenge(cid) on delete cascade, constraint part2_fk foreign key(uid) references user(uid) on delete cascade)')

cur.execute('show tables')

for i in cur:
    print(i)

# closing the connection
satisfy.close()