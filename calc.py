loop = 1

choice = 0

while loop == 1:
    print "Welcome to the Calculator"
    print "Your options are as follows:"
    print " "
    print "1) Addition"
    print "2) Subtraction"
    print "3) Multiplication"
    print "4) Division"
    print "5) Quit Program"
    print " "
    
    choice = input("Choose your option: ")
    if choice == 1:
        add1 = input("Add this: ")
        add2 = input("to this: ")
        print add1, "+", add2, "=", add1 + add2
    elif choice == 2:
        sub1 = input("Subtract this: ")
        sub2 = input("from this: ")
        print sub1, "-", sub2, "=", sub1 - sub2
    elif choice == 3:
        mul1 = input("Multiply this: ")
        mul2 = input("to this: ")
        print mul1, "*", mul2, "=", mul1 * mul2
    elif choice == 4:
        div1 = input("Divide this: ")
        div2 = input("from this: ")
        print div1, "/", div2, "=", div1 / div2
    elif choice == 5:
        loop = 0
        
print "Thank you for using the calculator."
