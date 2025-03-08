# Project Title: Python - Object-Relational Mapping (ORM)

![Project Badge](https://img.shields.io/badge/50.88%25-completed-blue)

## Overview
This project bridges two powerful worlds: Python and Databases. It introduces the concept of Object-Relational Mapping (ORM) by guiding you through the process of using Python to interact with a MySQL database. In this project, you will first work with raw SQL queries and then move to an ORM approach with SQLAlchemy to abstract away the underlying SQL commands, providing a cleaner, object-oriented interface to interact with databases.

## Author
Guillaume

## Weight
1

## Your score will be updated as you progress.

---

## Description

### Before You Start
Ensure your MySQL server is running version 8.0 or above. You can install MySQL 8.0 on Ubuntu 20.04 by following the [installation guide](https://dev.mysql.com/doc/refman/8.0/en/installing.html).

---

### Background Context

In this project, you'll get to experience two ways to interact with a MySQL database:

1. **Using raw SQL queries with MySQLdb**: This method involves directly executing SQL queries from Python code.
2. **Using SQLAlchemy ORM**: This method abstracts the database storage process and allows you to interact with the database as objects, not SQL statements. With ORM, you no longer need to worry about the SQL syntax; instead, you'll focus on interacting with your Python objects.

Example of querying a database without ORM:

```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

Example of querying a database with ORM (using SQLAlchemy):

```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
```

With ORM, you no longer write raw SQL queries but interact directly with objects, making the code cleaner and more flexible.

---

## Resources

### Read or Watch:

- [Object-Relational Mappers](https://www.google.com/search?q=object+relational+mappers)
- [mysqlclient/MySQLdb Documentation](https://mysqlclient.readthedocs.io/)
- [MySQLdb Tutorial](https://www.mysqltutorial.org/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [SQLAlchemy ORM Tutorial for Python Developers](https://realpython.com/python-sqlalchemy/)
- [Learning SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
- [SQLAlchemy Python Cheatsheet](https://cheat.readthedocs.io/en/latest/sqlalchemy/)

---

## Learning Objectives

By the end of this project, you should be able to:

### General Skills

- Connect to a MySQL database using Python
- SELECT rows from a MySQL table using Python
- INSERT rows into a MySQL table using Python
- Understand the concept of ORM and how it simplifies database interactions
- Map Python Classes to MySQL tables using SQLAlchemy

---

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files must be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- Your files should use MySQLdb version 2.0.x
- Your files should use SQLAlchemy version 1.4.x
- All files must end with a newline
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, placed at the root of the project folder, is mandatory
- Your code should follow the PEP 8 style guidelines (pycodestyle version 2.7.*)
- All files must be executable
- The length of your files will be tested using `wc`
- Every module, class, and function in your code should have proper documentation

---

## More Info

### MySQL Installation on Ubuntu 20.04

To install MySQL 8.0, use the following commands:

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

Once MySQL is installed, you can connect using:

```bash
$ sudo mysql
```

To exit MySQL:

```bash
mysql> quit
Bye
```

### Install MySQLdb (MySQL Client)

To install the MySQLdb module, run:

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```

Verify the installation:

```python
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy

To install SQLAlchemy, run:

```bash
$ sudo pip3 install SQLAlchemy
```

Verify the installation:

```python
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```

---

## Contributions

If you'd like to contribute to this project, feel free to fork the repository, create a branch, make your changes, and submit a pull request. All contributions are welcome!


