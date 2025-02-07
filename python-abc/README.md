Python OOP - Abstract Class, Interface, Subclassing
Introduction
Welcome to a series of exercises designed to strengthen your understanding and application of Object-Oriented Programming (OOP) concepts in Python. This set of tasks focuses on key principles such as abstract classes, interfaces, duck typing, subclassing, and more, enabling you to master OOP in Python and apply these concepts in real-world applications.

Learning Objectives
By completing these tasks, you will learn to:

Abstract Classes: Understand and apply abstract classes to define common interfaces and enforce certain class behaviors.
Interfaces and Duck Typing: Learn to use interfaces and duck typing to ensure objects adhere to a specific contract or protocol.
Subclassing Standard Base Classes: Extend built-in classes like lists and dictionaries to create custom data structures with specialized behavior.
Method Overriding: Modify or enhance the behavior of inherited methods through method overriding.
Multiple Inheritance: Grasp the power and complexities of multiple inheritance to create flexible class relationships.
Mixins: Leverage mixins to compose reusable behavior across unrelated classes.
Resources
Python 3 Object-Oriented Programming
ABC — Abstract Base Classes
Real Python - OOP in Python
Corey Schafer's OOP Playlist
Sentdex's Python OOP Tutorial
Tasks
0. Abstract Animal Class and its Subclasses
Background: Abstract Base Classes (ABCs) ensure derived classes implement specific methods. This task introduces you to abstract classes in Python using the abc module.
Objective:
Create an abstract Animal class with an abstract method sound.
Implement two subclasses Dog and Cat, each providing a specific implementation of the sound method.
Testing: Check that instantiating the abstract Animal class raises a TypeError.
1. Shapes, Interfaces, and Duck Typing
Background: Duck typing enables objects to be treated based on their behavior rather than their inheritance. This task will demonstrate abstract classes combined with duck typing.
Objective:
Create a Shape abstract class with methods area and perimeter.
Implement Circle and Rectangle classes that provide specific implementations for area and perimeter.
Define a function shape_info that prints the area and perimeter of any object adhering to the Shape interface.
Testing: Test the function with instances of Circle and Rectangle without checking their types explicitly.
2. Extending the Python List with Notifications
Background: In this task, you will extend Python's built-in list class to customize its behavior.
Objective:
Create a VerboseList class that overrides methods like append, extend, remove, and pop to print notifications each time an item is added or removed.
Testing: Instantiate VerboseList and perform various list operations to verify that the correct notifications are printed.
3. CountedIterator - Keeping Track of Iteration
Background: Subclassing iterators allows you to modify or enhance their functionality. This task involves keeping track of the number of iterations.
Objective:
Create a CountedIterator that extends the built-in iterator, counting how many times __next__ has been called.
Provide a get_count method to return the current count.
Testing: Use the CountedIterator on a list or iterable and verify the iteration count.
4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
Background: Multiple inheritance allows a class to inherit from multiple parent classes, which can complicate method resolution.
Objective:
Create Fish and Bird classes with basic methods (swim, fly, and habitat).
Implement a FlyingFish class that inherits from both Fish and Bird, overriding the methods to reflect the hybrid behavior.
Testing: Verify the correct method outputs from the FlyingFish instance and explore method resolution order (MRO).
5. The Mystical Dragon - Mastering Mixins
Background: Mixins are a way to compose behaviors in classes without creating rigid inheritance hierarchies.
Objective:
Create SwimMixin and FlyMixin classes with methods swim and fly.
Implement a Dragon class that inherits from both mixins, adding additional functionality like roar.
Testing: Instantiate the Dragon class and demonstrate its ability to swim, fly, and roar.
Repo
GitHub repository: holbertonschool-higher_level_programming
Directory: python-abc
File: task_00_abc.py, task_01_duck_typing.py, task_02_verboselist.py, task_03_countediterator.py, task_04_flyingfish.py, task_05_dragon.py