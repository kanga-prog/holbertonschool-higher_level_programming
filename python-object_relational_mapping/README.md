# Project README

## Before You Start

Please make sure that your MySQL server is running version 8.0. Here's a guide on how to install MySQL 8.0 on Ubuntu 20.04:

### How to Install MySQL 8.0 in Ubuntu 20.04
```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version  # Ensure it's MySQL 8.0.x
```

## Background Context

This project aims to bridge the worlds of Databases and Python! In this project, you'll explore two important ways of interacting with MySQL databases in Python:

1. **Using the `MySQLdb` module** (direct SQL queries).
2. **Using SQLAlchemy ORM** (abstracting away SQL queries into Python objects).

### Part 1: MySQLdb (Direct SQL Queries)

In the first part, you will connect to a MySQL database using `MySQLdb`, execute SQL queries, and manage the data directly with SQL syntax.

Example (without ORM):
```python
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")  # SQL Query
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

### Part 2: SQLAlchemy (Object Relational Mapper)

The second part focuses on using **SQLAlchemy**, an ORM that allows you to interact with the database using Python classes and objects instead of SQL queries. With SQLAlchemy, you no longer need to write raw SQL queries.

Example (with ORM):
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import State, Base

engine = create_engine('mysql+mysqldb://root:root@localhost/my_db', pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id).all():  # No SQL, only objects!
    print(f"{state.id}: {state.name}")
session.close()
```

### Key Difference:
- **Without ORM**: You write SQL queries to manipulate data.
- **With ORM**: You work directly with Python objects, and SQL is abstracted away.

## Resources

To better understand how to use MySQLdb and SQLAlchemy, you can explore the following resources:

- [Object-relational mappers](https://en.wikipedia.org/wiki/Object-relational_mapping)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/en/latest/)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [10 Common Stumbling Blocks for SQLAlchemy Newbies](https://realpython.com/python-sqlalchemy-tutorial/)
- [SQLAlchemy Cheatsheet](https://cheat.readthedocs.io/en/latest/sqlalchemy/)

## Learning Objectives

By the end of this project, you should be able to explain and demonstrate the following concepts:

1. How to connect to a MySQL database from a Python script.
2. How to SELECT rows in a MySQL table from Python.
3. How to INSERT rows into a MySQL table from Python.
4. What ORM is and how it abstracts the SQL layer.
5. How to map a Python class to a MySQL table using an ORM.

## Requirements

### General:
- **Allowed Editors**: vi, vim, emacs.
- All files will be executed on **Ubuntu 20.04 LTS** using Python 3.8.5.
- You must use **MySQLdb version 2.0.x** and **SQLAlchemy version 1.4.x**.
- All Python files should end with a new line.
- The first line of each Python file should be exactly: `#!/usr/bin/python3`.
- A **README.md** file is mandatory at the root of the project directory.
- Your code should follow the **pycodestyle** (version 2.7.*).
- All files must be executable.

### Documentation:
- All modules, classes, and functions must have proper documentation explaining their purpose.
- For example:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  python3 -c 'print(__import__("my_module").MyClass.__doc__)'
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  ```

### Restrictions:
- **You are not allowed to use `execute` with SQLAlchemy.**

## Installation

### 1. Install MySQL 8.0 on Ubuntu 20.04 LTS:
```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version  # Confirm MySQL version is 8.0
```

### 2. Install MySQLdb (MySQL Client for Python):
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```

### 3. Install SQLAlchemy:
```bash
$ sudo pip3 install SQLAlchemy
```

### 4. Check Installation:
After installation, confirm the versions:
```bash
$ python3
>>> import MySQLdb
>>> print(MySQLdb.version_info)

>>> import sqlalchemy
>>> print(sqlalchemy.__version__)
```

## Example MySQL Setup

To test your installation:

1. Connect to MySQL:
   ```bash
   $ sudo mysql
   ```
2. Create a test database and table:
   ```sql
   CREATE DATABASE my_db;
   USE my_db;

   CREATE TABLE states (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(50) NOT NULL
   );
   ```

3. Insert data into the table:
   ```sql
   INSERT INTO states (name) VALUES ("California"), ("Texas"), ("Florida");
   ```

Now you're ready to interact with this database using Python and either `MySQLdb` or `SQLAlchemy`.

## Conclusion

This project provides a solid introduction to working with MySQL databases in Python. By the end of this project, you should feel comfortable using both direct SQL queries and the SQLAlchemy ORM to manage database operations in your Python applications.


