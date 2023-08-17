class Car:
    window = 24
    count = 0

    def __init__(self, people):
        self.people = people
        self.window = 2
        self.wheel = 4
    
    def accelrate(self):
        print(f"{self.people}이(가) accelrate!")
    
    def brake(self):
        print(f"{self.people}이(가) brake!")
    
my_car = Car("김유진")
my_car.brake()

my_car1 = Car("김유진")
Car.count += 1
print(f"현재 생산된 자동차의 수: {Car.count}")

my_car2 = Car("김유진")
Car.count+=1
print(f"현재 생산된 자동차의 수: {Car.count}")
