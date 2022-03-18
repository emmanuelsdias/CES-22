def is_prime(n):
    """ Check if an integer n is prime or not """
    if (n < 2):
        return False
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

tests = [2, 5, 8, 13, 27]

for i in tests:
    if is_prime(i):
        print(i, "is prime.")
    else: 
        print(i, "isn't prime.")
    