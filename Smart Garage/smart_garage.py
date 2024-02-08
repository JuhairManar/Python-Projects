class Car:
    def __init__(self, license, model, color):
        self.license = license
        self.model = model
        self.color = color
    def __repr__(self):
        return f'{self.license},{self.model},{self.color}'

class Garage:
    def __init__(self):
        self.car_added=[]
        self.spot=1
        self.car_infos={}
        self.bill=0
        self.ticket=[]

    def spot_available(self):
        return f'Total spots available {self.spot}'

    def add_car_to_garage(self,car):
        self.spot_name = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1']
        if self.spot > 0:
            user_data = str(car).split(',') #str() is used for user readable
            self.spot-=1
            self.car_added.append(user_data)
            self.car_infos={'Tickets':[],"License":[],'Model':[],'Color':[]}
            ticket=""

            for i,val in enumerate(self.car_added):
                ticket=self.spot_name[i]+val[0]
                self.car_infos['Tickets'].append(ticket)
                self.car_infos['License'].append(val[0])
                self.car_infos['Model'].append(val[1])
                self.car_infos['Color'].append(val[2])
            print(f"Successfully Parked!!!Your Ticker {ticket}")
        else:
            print("Sorry,No spots available")  

    def unpark(self,ticket,hours):
        past_spot_len=len(self.car_infos['Tickets'])

        if ticket not in self.car_infos['Tickets']: #security check purpose
            print("NO CAR FOUND!!!!")
            return
        else:
            for i,val in enumerate(self.car_infos['Tickets']):
                if val==ticket:    
                    print(i)
                    print(f"Your license is {self.car_infos['License'][i]}")
                    print(f"Your license is {self.car_infos['Model'][i]}")
                    print(f"Your license is {self.car_infos['Color'][i]}")
                    
                    """ #Deleting method
                    self.car_infos['License'].pop(i)
                    self.car_infos['Model'].pop(i)
                    self.car_infos['Color'].pop(i)
                    self.car_infos['Ticket'].pop(i) """
                    self.spot+=1
        if hours >30:
            print(f"Total charge={hours*5+100}")
        else:
            print(f"Total charge={hours*5}")
    def total_cars_in_garage(self):
        for i in self.car_infos.items():
            print(i)        

       


my_garage=Garage()
""" 
user_car_1=Car("1234MN","Ferrari","Red")
user_car_2=Car("12TY","TOYOTA","BLUE")
#print(user_car)
my_garage.add_car_to_garage(user_car_1)
#my_garage.add_car_to_garage(user_car_2)
my_garage.unpark("A11234MN",10)
#my_garage.unpark("B112TY",10) """

while True:
    print("What do you want ?")
    print("1.Park your Car\n2.Check available space\n3.Unpark your car\n4.Total Cars in garage" )
    user_choice=int(input("Enter your choice: "))
    if user_choice==1:
        car_license = input("Enter your car license : ")
        car_model = input("Enter your car model : ")
        car_color = input("Enter your car color : ")
        user_car = Car(car_license, car_model, car_color) # Car class object
        my_garage.add_car_to_garage(user_car)
        print()
    elif user_choice==2: 
        print(my_garage.spot_available())   
    elif user_choice==3:
        ticket=input("Enter your ticket number: ")
        hours=int(input("Enter hours : "))
        if my_garage.unpark(ticket,hours):
            continue
        else:
            my_garage.unpark(ticket,hourse)
            print()
    elif user_choice==4:
        my_garage.total_cars_in_garage()  
    else:
        break       
