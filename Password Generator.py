import random
def password_generator():      #Function Creation:Reuse a block of code by calling a Function
      lower_case="abcdefghijklmnopqrstuvwxyz"
      upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      digits="1234567890"
      symbols="~!@#$%^&*(?/><["
      allchars= lower_case+upper_case+digits+symbols     
      length=input("Enter Length of Password:")     #Taking Input from users.
      if length.isdigit():        #If Condition Statement: If condition is true prints If satatement,otherwise prints else statement.
          length=int(length)
          if length > 0:
             password=''.join(random.choices(allchars,k=length))
          else:
             print("Invalid Choice:Length should be greater than zero.")
      else:
          print("Invalid choice: Please Enter a Number.")
      print("Genrated Password",password) 
password_generator()     #Calling a Function
      
