import my_module
print(my_module.greet("Alice"))
print(my_module.pi)

# or

from my_module import greet, pi

print(greet("Bob"))  # Output: Hello, Bob!
print(pi)  # Output: 3.14159