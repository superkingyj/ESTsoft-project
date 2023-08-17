from student import Student

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("학생 정보가 추가되었습니다!")

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student.get_info()
        print("해당 학생을 찾을 수 없습니다 !")
    
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                # 삭제하는 코드
                self.students.remove(student)
                print("학생 정보가 삭제되었습니다 !")
                return
        print("해당 학생을 찾을 수 없습니다 !")
        # for문이 끝난 후 해당값을 찾을 수 없을 때 실행

    def update_student(self, student_id, name, age):
        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                # 기존에 부여된 student.name은 사라지고 새로운 name이 생성된다
                student.age = age
                print("학생 정보가 수정되었습니다.")
                return
        print("해당 학생을 찾을 수 없습니다 !")