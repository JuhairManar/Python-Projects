from datetime import datetime     #to show the time         #it is package and second one is module
import uuid                       #to generate unique id    #it is a library


#the three dictionary needed is 
All_task={}    #to store all task
Comp_task={}   #to store all completed task
Incom_task={}  #to store all incompleted task

class Task:
    def __init__(self,task) -> None:
        self.task=task
        self.id=uuid.uuid1()     #assigning unique id
        self.updated_time="NA"   #as it is initialization it has no update time
        self.completed=False     #as it is initialization it completed is false
        self.completed_time="NA" #as it is initialization it ha s no completed time
        self.created_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def update_task(self,task):
        #first 4 line are for replace the key name 
        All_task[task]=All_task[self.task]      #assinging the values to other key
        del All_task[self.task]                 #delete tha previous key
        Incom_task[task]=Incom_task[self.task]  #assinging the values to other key
        del Incom_task[self.task]               #delete tha previous key
        #incomplete task dictionary is included because when a task is updated it is incompleted
        self.task=task                          #As the task is updated, the task name will be changes
        self.updated_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def complete_task(self):
        self.completed_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")     #Assigning the completion time
        self.completed=True                     #Assigning the completion status
        Comp_task[self.task]=f'ID - {self.id} \nTask - {self.task} \nCreated Time - {self.created_time} \nUpdate Time - {self.updated_time} \nCompleted - {self.completed} \nCompleted Time - {self.completed_time} \n' #assigning the values to the key
        Incom_task.pop(self.task)               #After a task is completed it must be removes from incompleted task dictionary
    
    def __repr__(self) -> str:
        return f'ID - {self.id} \nTask - {self.task} \nCreated Time - {self.created_time} \nUpdate Time - {self.updated_time} \nCompleted - {self.completed} \nCompleted Time - {self.completed_time} \n'     #to print all informations of a task
           
        

while True:                    #running a loop forver
    print("1. Add a new task")   
    print("2. Show all task")
    print("3. Show incomplete task")
    print("4. Show completed task")
    print("5. Update Task")    
    print("6. Mark as Task completed")
    op=int(input("Enter an option : "))  #option for user
    print('\n')
    
    if op==1: #Add a new task
        t=input("Enter new task: ")      #user will input a new task
        nt=Task(t)                       #creating an object of Task class
        All_task[t]=nt                   #All_task dictionary will have a keyword of value of t and the keyword's will have value nt
        Incom_task[t]=nt                 #the same operation with this list because, a new task is incompleted at the start
        print("\nTask created successfully")
        print('\n')
        
    elif op==2: #Show all task
        for k,v in All_task.items():    #printing all completed task with loop
            print(v)

    elif op==3 : #Show incomplete task
        if not Incom_task:              #checking is there is no incompleted task
            print("There is no incompleted task\n\n")
        else:                           #If there exist incompleted task
            print("The incompleted tasks are\n\n")
            for k,v in Incom_task.items():  #print the task
                print(v) 
                   
    elif op==4: #Show completed task
        if not Comp_task:                 #checking is there is no completed task
            print("There is no completed task\n\n")
        else:                             #If there exist completed task
            print("The completed tasks are\n\n")
            for k,v in Comp_task.items(): #print the task
                print(v)  
                 
    elif op==5: #Update Task
        i=1
        if not Incom_task:                  #checking is there is no incompleted task
            print("There is no task to update\n")
        else:                               #If there exist incompleted task
            print("Chosse which task to update\n")
            for k,v in Incom_task.items():  #print the incompleted task,because incompleted task needs to updated not the completed task
                print("Task no - ",i)       #to show the task number
                i+=1                        #the task number will be ascending order
                print(v)
            tu=int(input("Enter task no : ")) #which task number to update
            #print('\n')  
            i=1
            for k,v in Incom_task.items():    #searching the task with the number
                if i==tu:
                    new_task=input("Enter new task : ")  #update a task with new task
                    Incom_task[k].update_task(new_task)  #updated task isn't an completed task.it is an incompleted task
                    print("Task updated sucessfully\n")  #Message that the task is updated
                    break                                #after updating the task there is no use of the loop
                i+=1                                     #if the task not fount increment
    
    elif op==6: #Mark a Task completed
        i=1
        if not Incom_task:                    #checking is there is no incompleted task
            print("There is no task to complete\n")
        else:                                 #If there exist incompleted task
            print("Chosse an task to complete\n")
            for k,v in Incom_task.items():    #Showing the incompleted task,because only incompleted task can be completed
                print("Task no - ",i,'\n')
                i+=1                          #increament for task number
                print(v)                      #full details of incompleted task
            tu=int(input())                   #which task to complete  
            i=1
            for k,v in Incom_task.items():    #searching the task with the number
                if i==tu:
                    Incom_task[k].complete_task() #calling the complete_task function
                    print("Task completed sucessfully\n")
                    break
                i+=1
    
    else:
        print("Wrong input ---- Please enter a option again\n\n") #if user inputs an invalid option           
                    
                      
                                     
                
        
            
      
