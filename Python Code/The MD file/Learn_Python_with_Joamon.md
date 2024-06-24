Q1. What is Python?
ANS:

        A. Python is a very simple language, and has a very straightforward syntax. It encourages programmers to program without boilerplate (prepared) code. The simplest directive in Python is the "print" directive - it simply prints out a line (and also includes a newline, unlike in C).

        B. There are two major Python versions, Python 2 and Python 3. Python 2 and 3 are quite different. This tutorial uses Python 3, because it more semantically correct and supports newer features.

Q2. Variable and Types in Python?
ANS:

        A. Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

        B. Numbers:Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals). (It also supports complex numbers). Strings are defined either with a single quote or a double quotes.

Q3. What are List in Python?
ANS:

        A. Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.

        Q.1 What is append and extend?
        ANS: The append method is used to add a single element to the end of a list. This method modifies the original list in place and does not return a new list. It's a commonly used method when you want to dynamically build up a list by adding elements one at a time.

                * list.append(element)

                        a. list: The list to which you want to add an element.

                        b. element: The element you want to add to the end of the list.

                * Important Points

                        a. append adds a single element to the end of the list. If you need to add multiple elements, you can use extend or list concatenation.

                        b. The append method modifies the list in place and returns None.

                * Example of append vs. extend
                        a. append adds its argument as a single element to the end of a list.

                        b. extend iterates over its argument and adds each element to the list.

                * Example:      # Using append
                                        list1 = [1, 2, 3]
                                        list1.append([4, 5])
                                        print(list1)  # Output: [1, 2, 3, [4, 5]]

                                # Using extend
                                        list2 = [1, 2, 3]
                                        list2.extend([4, 5])
                                        print(list2)  # Output: [1, 2, 3, 4, 5]

Q4. Basic Operation in Python?
ANS:

        Python provides a wide range of basic operations that you can perform on various types of data. These operations include arithmetic operations, comparison operations, logical operations, and more. Here are some of the fundamental operations in Python:

        * Arithmetic Operations
        These operations are used to perform basic mathematical calculations.

                Addition (+):
                result = 3 + 2
                # Output: 5

                Subtraction (-):
                result = 5 - 2
                # Output: 3

                Multiplication (_):
                result = 4 _ 2
                # Output: 8

                Division (/):
                result = 8 / 2
                # Output: 4.0

                Floor Division (//):
                result = 7 // 2
                # Output: 3

                Modulus (%):
                result = 7 % 2
                # Output: 1

                Exponentiation (**):
                result = 2 ** 3
                # Output: 8

        * Comparison Operations
        These operations are used to compare two values.

                Equal (==):
                result = (3 == 3)
                # Output: True

                Not Equal (!=):
                result = (3 != 2)
                # Output: True

                Greater Than (>):
                result = (5 > 3)
                # Output: True

                Less Than (<):
                result = (2 < 3)
                # Output: True

        * Greater Than or Equal To (>=):

                result = (5 >= 5)
                # Output: True

                Less Than or Equal To (<=):
                result = (3 <= 4)
                # Output: True

        * Logical Operations
        These operations are used to combine conditional statements.

                Logical AND (and):
                result = (True and False) # Output: False

                Logical OR (or):
                result = (True or False) # Output: True

                Logical NOT (not):
                result = not True # Output: False

        * Bitwise Operations
        These operations are used to perform bit-level operations on integers.

                Bitwise AND (&):
                result = 5 & 3 # Output: 1 (binary: 0101 & 0011 = 0001)

                Bitwise OR (|):
                result = 5 | 3 # Output: 7 (binary: 0101 | 0011 = 0111)

                Bitwise XOR (^):
                result = 5 ^ 3 # Output: 6 (binary: 0101 ^ 0011 = 0110)

                Bitwise NOT (~):
                result = ~5 # Output: -6 (binary: NOT 0101 = 1010)

                Bitwise Left Shift (<<):
                result = 5 << 1 # Output: 10 (binary: 0101 << 1 = 1010)

                Bitwise Right Shift (>>):
                result = 5 >> 1 # Output: 2 (binary: 0101 >> 1 = 0010)

        * Assignment Operations
        These operations are used to assign values to variables.

                Assignment (=):
                x = 5 # Assigns 5 to x
                Add and Assign (+=):
                x = 5
                x += 3 # Equivalent to x = x + 3; x is now 8

                Subtract and Assign (-=):
                x = 5
                x -= 2 # Equivalent to x = x - 2; x is now 3

                Multiply and Assign (_=):
                x = 5
                x _= 2 # Equivalent to x = x \* 2; x is now 10

                Divide and Assign (/=):
                x = 5
                x /= 2 # Equivalent to x = x / 2; x is now 2.5

                Floor Divide and Assign (//=):
                x = 5
                x //= 2 # Equivalent to x = x // 2; x is now 2

                Modulus and Assign (%=):
                x = 5
                x %= 2 # Equivalent to x = x % 2; x is now 1

                Exponent and Assign (**=):
                x = 5
                x **= 2 # Equivalent to x = x \*\* 2; x is now 25

                Bitwise AND and Assign (&=):
                x = 5
                x &= 3 # Equivalent to x = x & 3; x is now 1

                Bitwise OR and Assign (|=):
                x = 5
                x |= 3 # Equivalent to x = x | 3; x is now 7

                Bitwise XOR and Assign (^=):
                x = 5
                x ^= 3 # Equivalent to x = x ^ 3; x is now 6

                Bitwise Left Shift and Assign (<<=):
                x = 5
                x <<= 1 # Equivalent to x = x << 1; x is now 10

                Bitwise Right Shift and Assign (>>=):
                x = 5
                x >>= 1 # Equivalent to x = x >> 1; x is now 2

        * Membership Operations
        These operations are used to test if a value is a member of a sequence (like strings, lists, or tuples).

                In (in):
                result = 3 in [1, 2, 3] # Output: True

                Not In (not in):
                result = 4 not in [1, 2, 3] # Output: True

        * Identity Operations
        These operations are used to compare the memory locations of two objects.

                Is (is):
                x = [1, 2, 3]
                y = x
                result = (x is y) # Output: True

                Is Not (is not)
                x = [1, 2, 3]
                y = [1, 2, 3]
                result = (x is not y) # Output: True

Q5. What is string formatting?
ANS:

        Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

        Here are some basic argument specifiers you should know:

               1. %s - String (or any object with a string representation, like numbers)

               2. %d - Integers

               3. %f - Floating point numbers

               4. %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

               5. %x/%X - Integers in hex representation (lowercase/uppercase)

        Q1. Basics of string operations
        ANS:

                1. Strings are bits of text. They can be defined as anything between quotes.

                Example:astring = "Hello world!"
                        print(astring.index("o"))

                2. That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character. Notice how there are actually two o's in the phrase - this method only recognizes the first.

                3. But why didn't it print out 5? Isn't "o" the fifth character in the string? To make things more simple, Python (and most other programming languages) start things at 0 instead of 1. So the index of "o" is 4.

                        print(astring.count("l"))

                4. That is a lowercase L, not a number one. This counts the number of l's in the string. Therefore, it should print 3.

                        print(astring[3:7])

                5. This prints a slice of the string, starting at index 3, and ending at index 6. But why 6 and not 7? Again, most programming languages do this - it makes doing math inside those brackets easier.

                6. If you just have one number in the brackets, it will give you the single character at that index. If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in. If you leave out the second number, it will give you a slice from the first number to the end.

                print(astring[-3:])

                6. You can even put negative numbers inside the brackets. They are an easy way of starting at the end of the string instead of the beginning. This way, -3 means "3rd character from the end".

                print(astring[3:7:2])

                Explanation:
                        start = 3: Start from index 3.
                        stop = 7: Stop at index 7 (but do not include the character at index 7).
                        step = 2: Take every second character from the start to stop indices.

                print(astring[::-1])

                7. There is no function like strrev in C to reverse a string. But with the above mentioned type of slice syntax you can easily reverse a string like this.

                print(astring.upper())
                print(astring.lower())

                8. These make a new string with all letters converted to uppercase and lowercase, respectively.

                astring2 = "Sagar Katekhaye"
                print(astring2.startswith("Sagar"))
                print(astring2.endswith("cvascfafcugv"))

                9. This is used to determine whether the string starts with something or ends with something, respectively. The first one will print True, as the string starts with "Hello". The second one will print False, as the string certainly does not end with "cvascfafcugv".

Q6. what are Conditions in Python?
ANS:

        Conditions are expressions that eveluate to either `True` or `False` and are primarily used in control flow statement to determine the path of execution in a program. These conditions are essential in constructing logic that allows programs to make decisions and execute different blocks of code based on the outcome of these evaluations.

        common used of Conditions:

                1. If Statements:
                        if condition:
                             # Code to execute if the condition is True.

                2. If-Else Statements:
                        if condition:
                                # Code to execute if the condition is True.
                        else:
                                # Code to execute if condition is False.

                3. Elif:(Else if)Statement
                        if condition 1:
                                # Code to execute if condition 1 is True.
                        elif condition 2:
                                # Code to execute if condition 2 is True.
                        else:
                                # Code to execute if none of the above conditions are True.

                4.  While Loops:
                        while condition:
                                # Code to execute as long as condition is True.

                5. For Loop with Conditional Statements:
                        for item in iterable:
                                if condition:
                                        # Code to execute if condition is True for the item.

This are the commmanly used conditions in Python.Now, let's have a look into the Types of conditions.

        Types Of Conditions:
                1. Comparison Operators: Used to Compare Values.
                        01.`==`: Equal to
                        02.`!=`: Not Equal to
                        03.`<`: Less than
                        04.`<=`: Less than or Equal to
                        05.`>`: Greater than
                        06.`>=`: Greater than or Equal to

                2. Logical/Boolean Operators: Used to combine multiple conditions.
                        01.`and`: True if both conditions are true.
                        02.`or`: True if one condition is true.
                        03.`not`: True if the condition is false.

                3. Membership Operators: Used to check membersship in sequence like list tuples, strings.
                        01.`in`: True if a value id found in the sequence.
                        02.`not in`: Ture if a value is not found in the sequence.

                4. Identity Operators: Used to compare the memory locations of two objects.
                        01.`is`: True if bothh variables point to the same objects.
                        02.`is not`: True if the variables do not point to the same object.

Q7. what are Loops, what two types of loops are there in Python?
ANS:

        Loops in Python are constructs that allows for the repeated execution of a block of code as long as a specified condition is met. They are essential for automating repetitive tasks, iterating over data structure and controlling the flow of a program based on dynamic conditions.

        Types od Looops in Python:

                There are Two primary types of loop in Python:
                        01. For Loops
                        02. While Loops

        1. For Loops:

                For loop are used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or any other iteration, the loop variable is assigned the next value in the sequence, and the block of code inside the loop is executed.

                Example: Syntax
                        for variable in sequence:
                                # Code to execute for each element in the sequence.

                Example:
                        fruit = ["apple", "banana", "cherry"]
                        for fruit in fruits:
                        print(fruit)

                        for i in range(5):
                        print(i)

        2. While Loop:

                While loop are used to execute a block of code as long as a specified conditions is true. the condition is evaluated before each iteration, and if it evaluates to `True`, the loop continues; otherwise, it stops.

                Example: syntax
                        while condition:
                                # Code to execute as long as the condition is True

                Example:
                        # print numbers from 1 to 5
                        count = 1
                        while count <= 5:
                        print(count)
                        count += 1

- "Break" and "Continue" Statements

        The `break` and `continue` statement are used to after the flow of loop in python. They provide a way to comtrol the loop's execution beyond the normal iteration behavior

        1. Break statement:

                The `break` statement is used to exit a loop prematurely. When the `break` ststement is encountered inside a loop, the loop terminates immediately, and control is transferred to the statement following the loop.

                Example:
                        # "break" and "Continue" statement
                        # print out 0,1,2,3,4
                        count = 0
                        while True:
                        print(count)
                        count += 1
                        if count >= 5:
                                break

        2. Continue Statement
                The `continue` statement is used to skip the rest of the code inside the loop for the current iteration and move to nect iteration of the loop. when `continue` is encountered, the loop does not terminate but proceeds to the next iteration,by pressing the remining code in the current iteration.

                Example:
                        # print out only odd numbers 1,3,5,7,9
                        for x in range(10):
                        # check if x is even
                        if x % 2 == 0:
                                continue
                        print(x)

- Can we use "else" clause for loops?

        Unlike laungage like C, CPP.. we can use else for loops. When the loop condition of "for" or "while" statement fails then code part in "else" is executed. If a break statement is executed inside the loop then the "else" part is skipped. Note that the "else" part is executed even if there is a continue statement.

        Example: # print out 1,2,3,4
                for i in range(1, 10):
                if(i%5==0):
                        break
                print(i)
                else:
                print("this is not printed because for loop is terminated of break but not of fail condition")

                Step-by-Step Execution
                Iteration 1: i = 1
                1 % 5 != 0, so print(1)
                Iteration 2: i = 2
                2 % 5 != 0, so print(2)
                Iteration 3: i = 3
                3 % 5 != 0, so print(3)
                Iteration 4: i = 4
                4 % 5 != 0, so print(4)
                Iteration 5: i = 5
                5 % 5 == 0, so break is executed and the loop terminates

        Loop Explanation:

                Range Function:

                range(1, 10) generates a sequence of numbers starting from 1 up to, but not including, 10. So, it produces the sequence: 1, 2, 3, 4, 5, 6, 7, 8, 9.

                For Loop:
                The for loop iterates over each number in this sequence.

                If Condition:
                Inside the loop, the condition if(i % 5 == 0) checks if the current number i is divisible by 5.
                If i is divisible by 5, the break statement is executed, which terminates the loop immediately.

                Print Statement:
                If the number is not divisible by 5, it is printed.

                Else Block:
                The else block associated with the for loop is executed only if the loop terminates normally (i.e., it completes all iterations without encountering a break statement).

Q8. What are Functions?
ANS:

        Functions are a convenient way to divide code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interface so programmers can share their code.

- How to write Functions in Python?

        Example:
                def block_head():
                        print("This is the block head: Example_function")

                        print("1st block line")
                        print("2nd block line")
                block_head()

        01. Where a block line is more Python code (even another block), and the block head is of the following format:
        block_keyword block_name(argument1,argument2,...) Block keywords we already know are "if", "for", and "while".

        02. Function in Python are defined using the block keyword "def", followed with the function's name as the block's name.

        03. Functions may also receive argumnt (variables passed from the caller to the function).

        04. Call Functions in Python.

                Example: def name_the_benefits_of_functions():
                        list_of_benefits = list_benefits()
                        for benefit in list_of_benefits:
                                print(build_sentence(benefit))

                A. name_the_benefits_of_functions(): This function prints out each benefit of functions in a formatted sentence.
                B. It first calls list_benefits() to get the list of benefits.
                C. Then, it iterates over each benefit in the list using a for loop.
                D. For each benefit, it calls build_sentence(benefit) to construct a sentence stating that the given benefit is a benefit of       functions.
                E. Finally, it prints each constructed sentence.

Q9. What are Classes and Objects?
ANS:

        1. Classes:
                A class is a blueprint or template for creating objects. It defines the properties(sttributes) and behaviots (methods) that objects of the class willhave. in other words, a class encapsulates data for object and the methods that operate on that data.

                Example:
                        class car:
                        # class variable
                        wheels = 4

                        # constructor
                        def __init__(self, make, model):
                        self.make = make
                        self.model = model

                        # Method
                        def drive(self):
                        print("The", self.make, self.model, "is driving.")

                In this example:
                                Car is a class representing cars.
                                It has attributes make and model.
                                It has a method drive() that defines the behavior of driving a car.

        2. Objects:
                An object is an instance of a class. It is a concrete realization of the blueprint defined by the class. When you create an object, you are creating a specific instance of that class, with its own unique data and behaviors.

                Example:
                        car1 = car("Toyota", "Camry")
                        car2 = car("Honda", "Accord")

                In this example:
                                `Car1` and `Car2` are object (instances) of the `Car` class.
                                Each object has it's own `make` and `model` attributes, specific to that instance.

        3. Key Point:

                1. Classes:
                        Blueprints or template for creating objects.
                        Define properties( attributes) and behaviors (Methods).

                2. Objects:
                        Instances of classses.
                        Repesent specific instance with unique data and behaviors.

                3. Encapsulation:
                        Classes encapsulate data and behaviour together, prompting modularity and resuability.

                4. Abstraction:
                        Classes provide abstraction by hiding the complex implementation detatils and exposing only the necessary features.

                5. Inheritance:
                       Classes can inherit attributes and methods from other classes, enabling code reuse and hierarcy.

                6. Polymorphism:
                        Object of different classes can be treated interchangeably if they share a common interface, promoting flexibility and extensibility.

Q.10 What is Dictionaries?
ANS:

        In Python, dictionaries are type of data structure that allow you to store and manage data in key_value pairs. They are one of the core data structures provided by Python and are extermely useful for a wide variety of applications, such as maintaining mappings, couting occurrences, and organizing data.

        Key Feature of Dictionaries

                1. Key-Value Pairs: Each entry in a dictionary consists of a key and its associated value.

                2. Unordered: Dictionaries are unordered collectons, meaning that the items do not have a define order.

                3. Mutable: Dictionaries can be modified after they are created; you can add, remove, and change key-values pairs.

                4. Unique Key: Keys in a dictionary must be unique. If you try to use a duplicate key, the new value will overwrite the existing value.

        Each Value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list,ect.) insteand of using its ondex to address it.

                Example: A dtdtbase of phone numbers could be stored using a dictionary like this:

                        phonebook = {}
                        phonebook["Sagar"] = 8655478564
                        phonebook["Kaustubh"] = 8564752263
                        phonebook["Shivam"] = 4654284155
                        print(phonebook)

                Alternatively, a dictionary can be initialized with the same values in following notiation:

                        phonebook = {
                                "Sagar" : 8985465465
                                "Kaustubh" : 54654945445
                                "Shivam" : 5465743246
                        }
                        print(phonebook)

        Iterating over dictionaries

                Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list, does not keep the order of the values stored in it. To iterate over key value pairs.

                Example:
                        phonebook = {"Sagar": 8985464489, "Kaustubh": 8745467895, "Shivam": 7854658984}
                        for name, number in phonebook.items():
                        print("phone number of %s is %d" % (name, number))

        Removing a value

                To remove a specified index, use either one of the following notations:

                Example:
                        phonebook = {
                                "Sagar" : 8985465465,
                                "Kaustubh" : 54654945445,
                                "Shivam" : 5465743246
                        }
                        del phonebook["Sagar"]
                        print(phonebook)
                or
                        phonebook = {
                                "Sagar" : 8985465465,
                                "Kaustubh" : 54654945445,
                                "Shivam" : 5465743246
                        }
                        phonebook.pop("Sagar")
                        print(phonebook)

        Exercise:

                phonebook = {
                                "Sagar" : 8985465465,
                                "Kaustubh" : 54654945445,
                                "Shivam" : 5465743246
                        }
                        print(phonebook)

        Dictionary Methods
                Dictionaries come with several built-in methods to help you work with them effectively:

               1. keys(): Returns a view object containing the keys of the dictionary.

               2. values(): Returns a view object containing the values of the dictionary.

               3. items(): Returns a view object containing the key-value pairs as tuples.

               4. get(key): Returns the value associated with key, or None if the key does not exist.

               5. pop(key): Removes the key and returns its value.

               6. update(dict): Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.

        Use Cases for Dictionaries
                Dictionaries are used in many different contexts:

                1. Configuration Settings: Storing configuration settings or options.

                2. Counting Occurrences: Counting the frequency of items in a dataset.

                3. Lookup Tables: Implementing fast lookups for data mapping.

                4. Structured Data: Storing and accessing structured data.

Q 10. What are Modules and Packages?
ANS:

        * Modules and Packages are essential components in Python that facilitate code organization, reuse, and ditribution

        A. Modules:
                1. A module is a single file (with a `.py` extension) that contains Python code. This code can define functions, classes, variables, and executable statements. Modules allow you to logically organize your Python code into separate files, making ir easier to manage and reuse.

                or

                1. In Programming, a module is piece of software that has a specific functionality. For example, when building a ping pong game, one module may be responsible for the game lofic, and another module draws the game on the screen. Each module consist of a different file, which may be edited separately.

                2. Module in Python are just Python file with a .py extension. the name of the module is the same as the file name. A Python module can have a set of functions, classes, or variables defined and implemented.

                mygame/
                        1. mygame/game.py
                        2. mygame/draw.py

                3. The Python script 'game.py' implements the game. It uses the function 'draw_game' from the file 'draw.py', or in other words, the 'draw' module that implements the logic for drawing the game on the screen.

                4. Modules are imported from other module using the 'import' command. In this example, the 'game.py' script may look something like this:

                Example:
                        # draw.py

                        def draw_gmae(result):
                        print(f"Drawing the game with result: {result}")

                        # game.py
                        # import the draw module
                        import draw

                        def play_game():
                        return "Victory"

                        def main():
                        result = play_game()
                        draw.draw_game(result)

                        # this means that if this script is executed, then
                        # main() will be executed
                        if __name__ == '__main__':
                        main()

                5. Importing module object to the current namespace
                        A namespace is a system where every object is named and can be accessed in Python. we import the function 'draw_game' into the main script's namespace by using the 'from' command.

                Example:
                        # game.py
                        # import the draw module
                        from draw import draw_game

                        def main():
                        result = play_game()
                        draw_game(result)

                You may have noticed that in this example, the name of the module does not precede draw_game, because we've specified the module name using the import command.

                The advantages of this notation is that you don't have to reference the module over and over. However, a namespace cannot have two objects with the same name, so the import command may replace an existing object in the namespace.

                6. Importing all objects from a module
                        You can use import * command to import all the objects in a module like this:

                Example:
                        # game.py
                        # import the draw module
                        from draw import *

                        def main():
                        result = play_game()
                        draw_game(result)

                This might be a bit risky as changes in the module may affect the module which imports it, but it is shorter, and doesn't require you to specify every object you want to import from the module.

                7. Customer import name
                        Module may be loaded uder any name you want. This is useful when importing a module conditionally to use same name in the rest of the code.

                        In Pythone, you can import a module using a custom name by using 'as' keyword. This can be particularly useful when you need to import modules conditionally or to avoid name conflicts

                        For example, if you have two draw module with slightly different names, tou may do the following:

                Example:
                        1. Basic syntax

                        import module_name as custom_name

                        2. Simple example

                        import numpy as np
                        arr = np.array([1,2,3,4,5])
                        print(arr)

                        In this example, the 'numpy' module is imported with the custom name'np'.

                        3. Conditional Import

                        If you need to import a module conditionally and use the same name throughtout your code, you can do something likr this:

                        import sys

                        if 'specific_module' in sys.modules:
                                import specific_module as my_module
                        else:
                                import alternative_module as my_module

                        my_module.some_function()

                Practical Example:

                        try:
                                import cPickle as pickle
                        except importError:
                                import pickle

                        data = {'key':'value'}
                        serialized_data = pickle.dumps(data)
                        print(serialized_data)
                        deserialized_data = pickle.loads(serialized_data)
                        print(deserialized_data)

                        4. Custom Import for Avoding Name Conflicts

                        If you have multile modules with the same function names, you can use custom import name to avoid conflicts:

                Example:
                        import module_one as mod1
                        import module_two as mod2

                        result1 = mod1.common_function()
                        result2 = mod2.common_function()

                8. Module Intialization
                        The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once. If another module in your code import the same module again, it will not be loaded again, so local variable inside the module act as "singleton", meaning they are initilized only once.
