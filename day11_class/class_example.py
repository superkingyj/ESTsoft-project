# class Ractangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    

#     def area(self):
#         return self.width * self.height

# rec = Ractangle(width=10, height=20)
# print(f"너비:{rec.width}, 높이:{rec.height}")
# print(rec.area())

class Animal():
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        pass

class Cat(Animal):
    legs_instance = 4 # 인스턴스 변수
    def __init__(self, sound, name, legs=4):
        self.legs_class = legs # 클래스 변수
        self.sound = sound
        self.name = name
    
    def sound_play(self):
        return print(f"{self.name}: {self.sound*2}")

class Dog(Animal):
    def __init__(self, sound, name, legs=4):
        self.legs = legs
        self.sound = sound
        self.name = name
    
    def sound_play(self):
        return print(f"{self.name}: {self.sound*3}")


# animals = [Cat(name="르미", sound="야옹"), Dog(name="스트", sound="쾅쾅")]
# for animal in animals:
#     animal.sound_play()

print(Cat("test", "test", 8).legs_class)
print(Cat("test", "test", 8).legs_instance)