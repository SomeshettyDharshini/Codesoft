contact_book = {}     

def add_contact():              # Function Creation(For Adding contacts)
  name = input("Enter contact name: ")      # Taking input from Users    
  phone = input("Enter phone number:+91 ")
  email = input("Enter email: ")
  contact_book[name] = {"phone": phone, "email": email}  # To Store the input's of user in a varaiable
 
def search_contact():      # Function Creation (For Searching Contacts)
  search_term = input("Enter name to search: ")
  for name, details in contact_book.items():     #For loop:Its allows to repeat a block of code multiple times.   
    if search_term in name:            #Conditional Statement(If): If condition is True prints If Statement otherwise it prints else statement.
      print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
      print("Name doesn't Found")
def display_contact():      # Function Creation (For Displaying contacts)
   print("\nAll Contacts:")
   for name,details in contact_book.items():
       print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
           
while True:        # While Loop: The While Loop runs as Long as a condition is satisfied.
  print("\nContact Book Menu:")
  print("1. Add Contact")
  print("2. Search Contact")
  print("3. Display Contacts")
  
  choice = input("Enter your choice: ")

  if choice == "1":            #
    add_contact()
  elif choice == "2":
    search_contact()
  elif choice == "3":
    display_contact()
  elif choice == "0":
    break
  else:
    print("Invalid choice")
    


