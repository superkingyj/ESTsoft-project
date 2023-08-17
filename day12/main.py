from student import Student
from student_management_system import StudentManagementSystem

def print_menu():
    print("\n======= 학생 관리 시스템 =======")
    print("1. 학생 추가")
    print("2. 학생 조회")
    print("3. 학생 수정")
    print("4. 학생 삭제")
    print("q. 종료")
    print("==============================")

def get_student_info_from_user():
    student_id = input("학번을 입력하세요: ")
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    return student_id, name, age

# 학생 관리 시스템 사용
sms = StudentManagementSystem()

while True:
    print_menu()
    choice = input("원하는 작업을 선택하세요: ")

    if choice == "1":
        student_id, name, age = get_student_info_from_user()
        student = Student(student_id, name, age)
        sms.add_student(student)
    elif choice == "2":
        student_id = input("조회할 학생의 학번을 입력하세요: ")
        result = sms.search_student(student_id)
        print(result)
    elif choice == "3":
        student_id = input("수정할 학생의 학번을 입력하세요: ")
        name = input("수정할 이름을 입력하세요: ")
        age = input("수정할 나이를 입력하세요: ")
        sms.update_student(student_id, name, age)
    elif choice == "4":
        student_id = input("삭제할 학생의 학번을 입력하세요: ")
        sms.delete_student(student_id)
    elif choice.lower() == "q":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 선택해주세요.")
