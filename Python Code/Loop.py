# For Loop
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# for loop can iterate over a sequence of number using the "rang" anb "xrange" functions. the difference betwwen range and xranger id that the range function returns
# a new list with numbers of that specified range, whereas xrange an iterator, which is more efficient. (python 3 used the range function, which acts like xrange).
# Note: the range function is zero based.

# print out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# print out 3,4,5
for x in range(3,6):
    print(x)

# print out 3,5,7
for x in range(3,8,2):
    print(x)

# While Loop

# print out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1 # this is the smae as count = count + 1

# "break" and "Continue" statement
# print out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# print out only odd numbers 1,3,5,7,9
for x in range(10):
    # check if x is even
    if x % 2 == 0:
        continue
    print(x)

# using "else" clause for loops
# print out 0,1,2,3,4 and then print "count value reached 5".

count = 0
while(count<5):
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))

# print out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated of break but not of fail condition")

# Step-by-Step Execution
    # Iteration 1: i = 1
    # 1 % 5 != 0, so print(1)
    # Iteration 2: i = 2
    # 2 % 5 != 0, so print(2)
    # Iteration 3: i = 3
    # 3 % 5 != 0, so print(3)
    # Iteration 4: i = 4
    # 4 % 5 != 0, so print(4)
    # Iteration 5: i = 5
    # 5 % 5 == 0, so break is executed and the loop terminates

# Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    print(number)