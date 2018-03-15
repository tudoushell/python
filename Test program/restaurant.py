class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describle_restaurant(self):
        print("this "+self.restaurant_name+"is very good "+self.cuisine_type+"there are "
        +str(self.number_served)+" people!")
    def open_restaurant(self):
        print("this restaurant is opening")
    def set_number_served(self,number):
        self.number_served=number
    def increment_number_served(self,number):
        self.number_served+=number
restaurant=Restaurant("happy restaurant","haha")
restaurant.set_number_served(10)
restaurant.describle_restaurant()
restaurant.open_restaurant()
# for i in range(1,3):
#     restaurant.increment_number_served(12)
#     restaurant.describle_restaurant()
class Say():
    def __init__(self,location="American"):
        self.location=location
    def display(self):
        print(self.location.title())
        
class Restaurant2(Restaurant):
    def __init__(self,name,decrible):
        super().__init__(name,decrible)
        self.location=Say()
    

test=Restaurant2("China","****")
test.describle_restaurant()
test.location.display()