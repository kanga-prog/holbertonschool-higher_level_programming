# Python Object Concepts

## 1. What is an object?
In Python, **everything is an object**. An object is a data structure that contains data (attributes) and behavior (methods). For example, numbers, strings, lists, functions, and even classes are objects.

## 2. Difference between a class and an object/instance
- **Class**: A blueprint for creating objects.
- **Object (or instance)**: A concrete occurrence of a class. You create an object by calling a class.

Example:
```python
class Dog:
    def bark(self):
        print("Woof!")

fido = Dog()  # fido is an instance of the Dog class
```

## 3. Difference between immutable and mutable objects
- **Immutable**: Cannot be changed after creation (e.g., `int`, `str`, `tuple`)
- **Mutable**: Can be changed after creation (e.g., `list`, `dict`, `set`)

## 4. What is a reference?
A **reference** is a variable that points to a location in memory where the object is stored.

## 5. What is an assignment?
**Assignment** binds a variable name to an object:
```python
a = [1, 2, 3]  # 'a' now refers to the list object [1, 2, 3]
```

## 6. What is an alias?
When two variables point to the **same object** in memory, they are aliases:
```python
a = [1, 2]
b = a  # b is now an alias of a
```

## 7. How to know if two variables are identical?
Use the `is` operator:
```python
a is b  # True if a and b point to the same object
```

## 8. How to know if two variables are linked to the same object?
Again, use `is`:
```python
a = [1, 2]
b = a
a is b  # True
```

## 9. How to display the variable identifier (memory address)?
Use the built-in `id()` function:
```python
print(id(a))  # Shows the memory address of the object
```

## 10. Mutable vs Immutable
- **Mutable** objects can be changed in-place.
- **Immutable** objects cannot be changed once created.

## 11. Built-in mutable types
- `list`
- `dict`
- `set`
- `bytearray`

## 12. Built-in immutable types
- `int`
- `float`
- `str`
- `tuple`
- `frozenset`
- `bytes`

## 13. How does Python pass variables to functions?
Python passes variables by **object reference** (sometimes called "pass-by-assignment"). The reference is passed by value:
- If the object is **mutable**, it can be changed inside the function.
- If it is **immutable**, the original cannot be modified.

Example:
```python
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4]
```
