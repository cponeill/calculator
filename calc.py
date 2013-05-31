def menu():
    print "Welcome to the Calculator"
    print "Your options are as follows:"
    print " "
    print "1) Addition"
    print "2) Subtraction"
    print "3) Multiplication"
    print "4) Division"
    print "5) Mean"
    print "6) Quit Program"
    print " "
    return input ("Choose your option: ")
    
def add(a,b):
    print a, "+", b, '=', a+b
    
def sub(a,b):
    print a, "-", b, '=', a-b
    
def mul(a,b):
    print a, "*", b, "=", a*b
    
def div(a,b):
    print a, "/", b, "=", a/b
    
def mean(a, b, c, d, e):
    print a, "+", b, "+", c, "+", d, "+", e, "/", 5, "=", a+b+c+d+e/5
    
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Add this: "), input("to this: "))
    elif choice == 2:
        sub(input("Subtract this: "), input("from this: "))
    elif choice == 3:
        mul(input("Multiply this: "), input("to this: "))
    elif choice == 4:
        div(input("Divide this: "), input("from this: "))
    elif choice ==5:
        mean(input("Add This: "), input("to this: "), input("and this: "), input("and this: "), input("finally this: "))
    elif choice == 6:
        loop = 0
        
print "Thank you for using the Casey Calculator. Please enjoy your day."    
