tasks=[]
def add_task(tasks):
    task=input("Add Task into To-DO List:")
    tasks.append(task)
    print(f"'{task}'added Successfully")
def view_task(tasks):
    print(f"'{tasks}' your Tasks")
def update_task(tasks):
    view_task(tasks)
    task_id=int(input("Enter the Number the Task to be Updated:"))  
    if 0<= task_id<len(tasks):
       new_task=input("Enter the new task:")
       tasks[task_id]=new_task
       print(f"'{new_task}' is updated Successfully")
    view_task(tasks)   
def delete_task(tasks):
     view_task(tasks)
     task_id=int(input("Enter the Number the Task to be deleted:"))
     if 0<= task_id<len(tasks):
         deleted_task=tasks.pop(task_id)
         print(f"'{deleted_task}' is deleted successfully")
     view_task(tasks)        
while True:
    print("To-do List Tasks: ")
    print("1.Add Task into List. ")
    print("2.View Task in List. ")
    print("3.Update Task in List. ")
    print("4.Delete Task from List. ")
    choice=int(input("Enter your Choice:"))
         
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
        
    
    
