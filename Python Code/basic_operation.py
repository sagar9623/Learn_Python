number = 1 + 2 * 3 / 4.0
print("number: %f" % number)

reminder = 11 % 3
print("reminder: %d " % reminder)

squared = 7 ** 2
cubed = 2 **3
print("squared: %d" % squared)
print("cubed: %d" % cubed)

x = object()
y = object()

x_list = [x] * 7
y_list = [y] * 15
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 7 and y_list.count(y) == 15:
    print("Almost there...")

if big_list.count(x) == 15 and y_list.count(y) == 15:
    print("Great!")