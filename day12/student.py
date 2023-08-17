class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name= name
        self.age = age
    
    def get_info(self):
        return f"학번: {self.student_id}, 이름: {self.name}, 나이: {self.age}"