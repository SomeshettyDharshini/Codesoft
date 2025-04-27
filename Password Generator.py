import random
def password_generator():
      lower_case="abcdefghijklmnopqrstuvwxyz"
      upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      digits="1234567890"
      symbols="~!@#$%^&*(?/><["
      allchars= lower_case+upper_case+digits+symbols
      length=input("Enter Length of Password:")
      if length.isdigit():
          length=int(length)
          if length > 0:
             password=''.join(random.choices(allchars,k=length))
          else:
             print("Invalid Choice:Length should be greater than zero.")
      else:
          print("Invalid choice: Please Enter a Number.")
      print("Genrated Password",password) 
password_generator()
      
