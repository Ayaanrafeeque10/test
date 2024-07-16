def factorial_while(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        fact = 1
        while n > 0:
            fact *= n
            n -= 1
        return fact
def main():

    num = int(input("Enter a number to calculate its factorial: "))
    result = factorial_while(num)
    print(f"The factorial of {num} is: {result}")

if __name__ == "__main__":
    main()
