# Python Exceptions - Project

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- **Why Python programming is awesome**  
  Python is an easy-to-read, high-level language with a rich set of libraries and frameworks, making it a great choice for rapid development and experimentation.

- **What’s the difference between errors and exceptions**  
  - Errors are usually issues in the code that can cause the program to stop running, such as syntax errors.  
  - Exceptions are events that can happen during the execution of a program that disrupt the normal flow. Exceptions can be handled and recovered from.

- **What are exceptions and how to use them**  
  Exceptions are events that disrupt the flow of the program. They are typically errors that can be handled gracefully using try and except blocks.

- **When do we need to use exceptions**  
  We use exceptions when an error might occur that could stop the program from executing. Instead of allowing the program to crash, exceptions help us manage the error and proceed with the program.

- **How to correctly handle an exception**  
  Exceptions can be handled using a `try` block followed by an `except` block. The `try` block contains code that may throw an exception, and the `except` block contains code to handle the exception.

- **What’s the purpose of catching exceptions**  
  The purpose of catching exceptions is to prevent the program from crashing and to handle errors gracefully, providing an opportunity to correct the issue or notify the user.

- **How to raise a builtin exception**  
  Python provides built-in exceptions that can be raised using the `raise` keyword. For example, `raise ValueError("Invalid input!")`.

- **When do we need to implement a clean-up action after an exception**  
  Clean-up actions are necessary when resources (like files or network connections) need to be released after an exception is handled. This is often done using the `finally` block.

## Requirements

### General

- **Allowed editors**: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` (version 2.7.*).
- All your files must be executable.
- The length of your files will be tested using `wc`.

## Tasks

### 0. Safe Print List

Write a function that prints `x` elements of a list. The function should handle the case where `x` might be larger than the number of elements in the list.

Prototype: `def safe_print_list(my_list=[], x=0):`

- The function should print elements on the same line, followed by a new line.
- If `x` exceeds the length of the list, it should not throw an error, but should print as many elements as possible.
- The function should return the real number of elements printed.
- You should use `try` and `except` to handle potential errors.

### 1. Safe Print Integer

Write a function that prints an integer safely.

Prototype: `def safe_print_integer(value):`

- The function should print an integer, and handle exceptions if the value is not an integer.
- If the value is not an integer, it should print nothing and return `False`.
- If the value is an integer, it should return `True`.

### 2. Divide List

Write a function that divides two integers safely.

Prototype: `def safe_divide(a, b):`

- The function should divide `a` by `b`, but handle the case when division by zero occurs.
- If `b` is zero, the function should return `None`.

## Installation

To use this project:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-exceptions.git
