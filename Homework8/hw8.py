#1---------------------------------

n = int(input("Enter your digit>>>"))
def count_divisible_by_three (n):
    if n <= 0:
        print("Enter non-negative number")
    count = 0
    while n > 0:
        d = n % 10
        if d % 3 == 0 and d != 0:
            print(d)
            count += 1
        n = n // 10
    return count

res = count_divisible_by_three(n)
print("Quantity:", res)

#2-----------------------------------

num1 = int(input("Enter first number>>>"))
num2 = int(input("Enter second number>>>"))
def lcm(a, b):
    m = max(a, b)
    while True:
        if m % a == 0 and m % b == 0:
            return m
        m += 1

print(lcm(num1, num2))

#3--------------------------------------

star_count = int(input("Enter star qty>>>"))
def print_stars(stars):
    i = 0
    while i < stars:
        print("*", end="")
        i += 1
    print()
print_stars(star_count)

#4--------------------------------------

f_num = int(input("Enter number for factorial>>>"))
def factorial(number):
    res = 1
    i = 1
    while i <= number:
        res *= i
        i += 1
    return res

print(factorial(f_num))

#5---------------------------------------

def print_stars(stars, column):
    i = 1
    while i <= stars:
        print("*", end="")
        if i % column == 0 and i != stars:
            print()
        i += 1
    print()
s_count = int(input("Enter qty stars for print>>>"))
c_count = int(input("Enter column number>>>"))
print_stars(s_count, c_count)

