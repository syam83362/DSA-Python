# recursion => A function calling it self to solve a problem
# Two important parts of recursion is base case and recursive case
# if we do not handle the base case correctly, it will become a infinate loop


def print_numbers(n):
    if n>5:
        return #base case
    print(n)
    print_numbers(n+1) # recursive case

print("print numbers")
print_numbers(1)

# factorial of a number example

def factorial(n):
    if n == 0 or n == 1 :
        return 1
    return n * factorial(n-1)

print("factorial")
print(factorial(7))

# fabinocci series

def fabinoci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fabinoci(n-1)+fabinoci(n-2)

print("fabinoci")
print(fabinoci(10))

# sum of individual numbers

def sum_of_digits(n):
    if n == 0:
        return 0
    return n%10+sum_of_digits(n//10)

print("sum of digits")
print(sum_of_digits(711))

## recursion advanced

# for the previous recursion, after the function call in the recursive case
# there still needed things to done in factorial after the fumction call the result should be mltiplied by the n
# here in recursive tail there is no need

def factorial_tail(n,accumilator=1):
    if n == 0 or n == 1 :
        return accumilator
    return factorial_tail(n-1,accumilator*n)

print("factorial_tail")
print(factorial_tail(7))

# for large ammount of variables the loops are the sufficient and for claer and clean code the recurssion is good