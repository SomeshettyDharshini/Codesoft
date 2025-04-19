n1=int(input("Enter First Number: "))
operator=input("Enter an Operator:")
n2=int(input("Enter Second Number: "))
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
