# num = int(input("Enter a number: "))

def factorial(n):
    fact = 1
    if n==0:
        return 1
    elif n<0:
        return "Invalid"
    else:
        # return n*factorial(n-1)
        for i in range(1,n+1):
            fact *= i
        return fact

# result = factorial(5)
print(f"Factorial of 5 is {factorial(5)}")
