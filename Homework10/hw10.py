#1-------------------------------------------------
str = input("Enter your word>>>")
char = input("Enter letter for searching>>>")
def char_count(str:str, char:str)->int:
    i = 0
    found = 0
    while i < len(str):
        if str[i] == char:
            found += 1
        i += 1
    return found
print(char_count(str,char))

#2--------------------------------------------------

def print_str_with_space(str:str)->None:
    i = 0
    while i < len(str):
        print(str[i], end=" ")
        i += 1
    return
print_str_with_space("hello")
print()

#3----------------------------------------------------

a = int(input("Enter your number>>>"))
def reverse_number(number:int):
    i = 1
    number = f"{number}"
    while i <= len(number):
        print(number[-i], end=" ")
        i += 1
(reverse_number(a))