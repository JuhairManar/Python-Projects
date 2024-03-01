import hashlib
from random import random,randint,choice
from brta import BRTA
from vehicles import Bike, Car, CNG
from ride_manager import uber
import threading

class UserAlreadyExists(Exception):
    def __init__(self, email, *args: object) -> None:
        print(f'User: {email} already exists.')
        super().__init__(*args)

license_authority=BRTA()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.sha256(password.encode()).hexdigest()
        already_exists = False
        try:
            with open('users.txt', 'r') as file:
                if email in file.read():
                    already_exists = True
        except FileNotFoundError:
            pass

        # if already_exists:
        #     raise UserAlreadyExists(email)

        with open('users.txt', 'a') as file:
            file.write(f'{email} - {pwd_encrypted}\n')

    @staticmethod
    def log_in(email, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            with open('users.txt', 'r') as file:
                for line in file:
                    if email in line:
                        stored_password = line.split('- ')[1].strip()
                        break
        except FileNotFoundError:
            return 'invalid user'

        if hashed_password == stored_password:
            print('valid user')
        else:
            print('invalid user')    

class Rider(User):
    def __init__(self, name, email, password, location, balance):
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance
        self.__trip_history = []

    def set_location(self, location):
        self.location = location
    
    def get_location(self):
        return self.location
    
    def request_trip(self, destination):
        pass
    
    def get_trip_history(self):
        return self.__trip_history
    
    def start_a_trip(self, fare, trip_info):
        print(f'A trip started for {self.name}')
        self.balance -= fare
        self.__trip_history.append(trip_info)

class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
        self.vehicle = None
    
    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            self.license = None
        else:
            self.license = result
            self.valid_driver = True    

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver:
            if vehicle_type.lower() == 'car':
                self.vehicle = Car(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            elif vehicle_type.lower() == 'bike':
                self.vehicle = Bike(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            else:
                self.vehicle = CNG(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
        else:
            pass
    
    def start_a_trip(self, start, destination, fare, trip_info):
        self.earning += fare
        self.location = destination
        trip_thread = threading.Thread(target=self.vehicle.start_driving, args=(start, destination,))
        trip_thread.start()
        self.__trip_history.append(trip_info)
        
# trip_thread = threading.Thread(target=self.vehicle.start_driving, args=(start, destination,))
    
rider1=Rider('rider1','rider1@gmail.com','rider1',randint(0,30),1000)
rider2=Rider('rider2','rider2@gmail.com','rider2',randint(0,30),5000)
rider3=Rider('rider3','rider3@gmail.com','rider3',randint(0,30),5000)
rider4=Rider('rider4','rider3@gmail.com','rider4',randint(0,30),5000)
rider5=Rider('rider5','rider3@gmail.com','rider5',randint(0,30),5000)


vehicle_types = ['car', 'bike', 'cng']

for i in range(1, 100):
    driver1 = Driver(f'driver{i}', f'driver{i}@gmail.com', f'driver{i}', randint(0, 100), randint(1000, 9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle(choice(vehicle_types), randint(10000, 99999), 10)


print(uber.get_available_cars)
uber.find_a_vehicle(rider1,choice(vehicle_types),randint(1,100))
uber.find_a_vehicle(rider2,choice(vehicle_types),randint(1,100))
uber.find_a_vehicle(rider3,choice(vehicle_types),randint(1,100))
uber.find_a_vehicle(rider4,choice(vehicle_types),randint(1,100))
uber.find_a_vehicle(rider5,choice(vehicle_types),randint(1,100))

print(rider1.get_trip_history())
print(uber.total_income())