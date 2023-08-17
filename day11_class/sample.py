class HealthCheck:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def check_health(self):
        bmi = self.calculate_bmi()
        self.bmi = bmi
        result = self.get_result(bmi)

        print("=== 건강검진 결과 ===")
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")
        print(f"신장: {self.height}cm")
        print(f"체중: {self.weight}kg")
        print(f"BMI: {bmi:.2f}")
        print(f"결과: {result}")

    def calculate_bmi(self):
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return bmi

    def get_result(self, bmi):
        if bmi < 18.5:
            return "저체중"
        elif 18.5 <= bmi < 23:
            return "정상체중"
        elif 23 <= bmi < 25:
            return "과체중"
        elif 25 <= bmi < 30:
            return "경도비만"
        else:
            return "고도비만"
    
    def backup_records(self):
        with open(f"backup_{self.name}.txt", "a+") as file:
            file.write(self.name + "\n" + \
                       str(self.age) + "\n" + \
                       str(self.height) + "\n" + \
                       str(self.weight) + "\n" + \
                       str(self.bmi) +"\n")
    
my_patient1 = HealthCheck("김유진", 26, 165, 54)
my_patient2 = HealthCheck("김유진", 27, 165, 54)
my_patient3= HealthCheck("김유진", 13, 165, 54)
my_patient4 = HealthCheck("김유진", 30, 165, 54)

my_patients = [my_patient1, my_patient2, my_patient3, my_patient4]
print(sum([my_patient.age for my_patient in my_patients])/len(my_patients))