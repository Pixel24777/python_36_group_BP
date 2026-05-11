#1-----------------------

digits_=int(input("Please enter your digits>>>"))
def digits(num):
    if type(num) is not int:
        print("please enter integer")
        return -1
    if num == 0 or num < 0:
        print("Error. Please enter a positive number.")
        return -1
    def rec (n):
        if n==0:
            return -1
        rec(n//10)
        print(n%10)
    rec(num)
print(digits(digits_))

#2-----------------------------

a = int(input("Please enter your number>>>"))
def is_prime_number(number:int)->bool:
    i = 2
    if type(number) is not int:
        print("Please enter integer")
        return False
    if number == 0:
        print("Error")
        return False
    if number < 0:
        number =- number
    if number ==1:
        return print("False 1 is not prime") and False
    while i < number:
        if number % i == 0:
            print(f"{number} is not prime ")
            return False
        i+=1
    print(f"{number} is prime")
    return True
print(is_prime_number(a))

#3----------------------------------------------------------

luck = int(input("Enter your numbers>>>"))
def is_lucky_number (number):
    if type(number) is not int:
        print("please enter integer")
        return -1
    if number == 0 or number < 0:
        print("Error. Please enter a positive number.")
        return -1
    res_odd= 0
    res_even=0
    count = 1
    while number > 0:
        res = number % 10
        number //= 10
        if count % 2 == 0:
            res_even += res
        else:
            res_odd += res
        count += 1
    return res_odd == res_even
print(is_lucky_number(luck))

#4----------------------------------------------------------------

res = int(input("Enter digits>>>"))
def count_digits(number):
    if type(number) is not int:
        print("Enter integer")
        return -1
    if number < 0:
        number = - number
    count = 1
    while number > 9:
        count += 1
        number //= 10
    return count
print(count_digits(res))
