from email.mime import audio


class parking_lot:
    def __init__(self) -> None:
        self.total_parking=5

class Owner:
    def __init__(self,cn) -> None:
        self.car_name=cn

""" def charge(time):
    return time*5 """

class Dealing:
    def __init__(self) -> None:
        self.tc=0
    def charge(self,time):
        if(time>20):
            self.tc=(time*5)+50
            return f'{self.tc}$'    
        self.tc=time*5
        return f'{self.tc}$'

    def change(self,amount):
        return  f'{amount-self.tc}$'   

all_Owners=[]
pl=parking_lot()
dl=Dealing()

while True:
    print("What do you want___\n1.Enter\n2.Out")
    op=int(input())
    if op==1:
        if pl.total_parking==0:
            print("Sorry,No parking space left")
        else:
            print("Enter your car name")
            car_name=input()
            Current_Owner=Owner(car_name)
            all_Owners.append(Current_Owner)   
            pl.total_parking-=1 
        

    else:
        if pl.total_parking==5:
            print("Invalid Operation,the parking lot is totally empty")
            continue
        print("Enter your car name")
        car_name=input()
        found=False
        for i in all_Owners:
            if i.car_name==car_name:
                found=True
                Current_Owner=i
                print("Please tell us your parking duration")
                d=int(input())
                total_charge=dl.charge(d)
                print("Your total charge is ",total_charge)
                print("Plase enter your amount")
                amount=int(input())
                back=dl.change(amount)
                print("Your return is ",back)
                pl.total_parking+=1
                all_Owners.remove(Current_Owner)
                continue



        if found==False:
            print("You theif!!Security catch this man.")


1
BMW
1
Audi
2
Audi
6


