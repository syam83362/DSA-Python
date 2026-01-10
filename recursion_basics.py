# recursion => A function calling it self to solve a problem
# Two important parts of recursion is base case and recursive case
# if we do not handle the base case correctly, it will become a infinate loop


def print_numbers(n):
    if n>5:
        return #base case
    print(n)
    print_numbers(n+1) # recursive case

print_numbers(1)

# factorial of a number example

def factorial(n):
    if n == 0 or n == 1 :
        return 1
    return n * factorial(n-1)


print(factorial(7))