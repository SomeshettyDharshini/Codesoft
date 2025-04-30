#Taking inputs from the user
n1=int(input("Enter First Number: "))
operator=input("Enter an Operator:")
n2=int(input("Enter Second Number: "))
#Conditional Statement (elif) :If one condition is not satisfied its check with another(elif) condition ,if not prints else Statement.
if operator=='+':
    print("n1+n2=",n1+n2)
elif operator=='-':
        print("n1-n2=",n1-n2)
elif operator=='*':
        print("n1*n2=",n1*n2)
elif operator=='/':
        print("n1/n2=",n1/n2)
elif operator=='%':
        print("n1%n2=",n1%n2) 
elif operator=='**':
        print("n1**n2=",n1**n2) 
else:
     print("Invalid Operator ")
