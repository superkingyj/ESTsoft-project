class Car:
    def  __init__(self, model, car_type="electric"):
          self.model = model
          self.wheel = 4
          self.speed = 50
          self.car_type = car_type
    def brake(self):
          self.speed -= 50
    def accelerate(self):
          self.speed += 50

my_car = Car("Tesla")
my_car.accelerate()
my_car.accelerate()
my_car.brake()
print(my_car.model, my_car.wheel, my_car.speed)
