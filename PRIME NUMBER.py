def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
n = int(input("Enter a number: "))
if is_prime(n):
    print("Prime")
else:
    print("Not prime")
