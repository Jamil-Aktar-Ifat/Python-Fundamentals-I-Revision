import math
user_input = int(input("Upper limit for prime numbers: "))


def is_prime(num):
    for i in range(2, int(math.sqrt(num) +1)):
        if num % i == 0:
            return False
    return True
        
for i in range(1, user_input + 1):
    if is_prime(i):
        print(i)
