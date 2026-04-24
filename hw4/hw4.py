def f1():
    print("f1", end=" ")
    f4()

def f2():
    print("f2", end=" ")
    f6()

def f4():
    print("f4", end=" ")
    f5()

def f5():
    print("f5", end=" ")
    f6()

def f6():
    print("f6")

def main():
    print("main", end=" ")
    f6()
    print("main", end=" ")
    f1()
    print("main", end=" ")
    f2()

main()
#Questions
"""
1 - only three functions called by main (f6, f1, f2) 
2 - only 'Function 3' 
3 - only three functions (f2, f3, f6) 
"""