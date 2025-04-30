tasks=[]
#Function Creation :Reuse the block of code ,by calling a function.
def add_task(tasks):         #Function for Adding Tasks
    task=input("Add Task into To-DO List:")
    tasks.append(task)
    print(f"'{task}'added Successfully")
def view_task(tasks):         #Function For Viewing Tasks
    print(f"'{tasks}' your Tasks")
def update_task(tasks):      #Function Updating Tasks
    view_task(tasks)
    task_id=int(input("Enter the Number the Task to be Updated:"))  
    if 0<= task_id<len(tasks):   #If Statement 
       new_task=input("Enter the new task:")
       tasks[task_id]=new_task
       print(f"'{new_task}' is updated Successfully")
    view_task(tasks)   
def delete_task(tasks):    #Function For Deleting Tasks
     view_task(tasks)
     task_id=int(input("Enter the Number the Task to be deleted:"))
     if 0<= task_id<len(tasks):
         deleted_task=tasks.pop(task_id)
         print(f"'{deleted_task}' is deleted successfully")
     view_task(tasks)        
while True:      #While Loop: While loop runs as long as a condition is True.
    print("To-do List Tasks: ")
    print("1.Add Task into List. ")
    print("2.View Task in List. ")
    print("3.Update Task in List. ")
    print("4.Delete Task from List. ")
    choice=int(input("Enter your Choice:"))
    #Conditional statement (elif): If one condition is not satisfied ,it checks another elif sattement ,if not prints else statement.
    if choice==1:
      add_task(tasks)
    elif choice==2:
      view_task(tasks)
    elif choice==3:
      update_task(tasks)
    elif choice==4:
      delete_task(tasks)
    else:
      print("Invalid Choice")
        
    
    
