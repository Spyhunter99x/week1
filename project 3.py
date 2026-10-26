
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

def check_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

print("Number is:", check_even_odd(num))

if check_prime(num):
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")
