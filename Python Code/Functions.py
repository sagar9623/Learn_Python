# How to write Functions in Python?

# Example:
def block_head():
    print("This is the block head: Example_function")
                
    print("1st block line")
    print("2nd block line")
block_head()

def my_function():
    print("Hello from My Function!")
    my_function()

# Functions may also receive argument (variables passed from the caller to the function).

# Example !:
def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"% (username, greeting))
my_function_with_args("Kaustubh", "a great day")

# Example 2:

def my_function_the_args(username, greeting):
    # 1st block line
    print(f"{greeting}, {username}!")
    # 2nd block line
    print("This is a personalized greeting.")
    # additional block line (if needed)
    print("Hope you have a great day!")

my_function_the_args("Sagar", "Good Morning")
my_function_the_args("Kaustubh", "Good Morning")

# Function may return a value to the caller, using the keyword- "return".

def sum_of_two_numbers(a, b):
    return a + b
result1 = sum_of_two_numbers(15, 69)
result2 = sum_of_two_numbers(45, 87)
result3 = sum_of_two_numbers(89, 93)

print("The sum of 15 and 69 is:", result1)
print("The sum of 45 and 87 is:", result2)
print("The sum of 89 and 93 is:", result3)

# How do we call Functions in Python?

def my_function():
    print("Hello from My Function!")
def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function! I wish you %s" % (username, greeting))
def sum_of_two_numbers(a, b):
    return a + b
my_function()
my_function_with_args("Sagar Katekhaye", "a great year!")
x = sum_of_two_numbers(89,54)
print("The sum of 89 and 54 is:", x)

# Exercise:

def list_benefits():
    return ["More organized code",
            "More readable code",
            "Easier code reuse",
            "Allowing programmers to share and connect code together"]
def build_sentence(benefit):
    return ("%s is a benefit of function!" % benefit)
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
name_the_benefits_of_functions()