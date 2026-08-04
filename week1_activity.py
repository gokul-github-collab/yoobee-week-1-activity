
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    result = 1
    for i in range(1,n + 1):
        result *= i

    return result



if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    print(fibonacci(user_input))

    print(f'Factorial of {user_input}: {factorial(user_input)}')