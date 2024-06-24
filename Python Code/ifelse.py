def check_weirdness(n):
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <=5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
            
n = 3
check_weirdness(n)

n = 24
check_weirdness(n)