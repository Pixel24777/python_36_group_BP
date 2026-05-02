#1---------------------------------------------------

speed = int(input("Choose a fan mode>>>"))
def fan(mode: int) -> str:
    if mode < 0 or mode > 3:
        return("Error: invalid mode. Please enter 0, 1, 2 or 3")
    if mode == 1:
        return("Fan is running at speed 1")
    if mode == 2:
        return("Fan is running at speed 2")
    if mode == 3:
        return("Fan is running in turbo mode")
    if mode == 0:
        return("Fan is turned off")
print(fan(speed))

#2------------------------------------------------------

a = int(input("Enter your number>>>"))
def even_or_odd(number):
    if number %2 == 0:
        print("The number is even")
    else :
        print("The number is odd")
print(even_or_odd(a))

#3------------------------------------------------------
b = int(input("Enter age>>>"))
def my_age(age):
    if age < 0:
        return "Error: Age cannot be negative"
    elif age <= 18:
        return "Child"
    elif age <= 67:
        return "Adult"
    elif age > 67:
        return "Senior"
    else :
        return
print(my_age(b))