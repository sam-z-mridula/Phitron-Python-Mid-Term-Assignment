class StudentDatabase:
    student_list = []

    def add_student(self, student_id, name, department, is_enrolled):
        student = Student(student_id, name, department, is_enrolled)
        self.student_list.append(student)


class Student(StudentDatabase):
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    def enroll_student(self, id):
        if self.__is_enrolled == True:
            print(f'\nStudent {id} is already enrolled')
        else:
            self.__is_enrolled = True
            print(f'\nStudent {st_id} has been successfully enrolled')

    def drop_student(self):
        self.__is_enrolled = False

    def view_student_info(self):
        text = f'ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}'
        print(text)



s1 = Student('s101', 'Alice Smith', 'Computer Science', True)
s2 = Student('s102', 'Bob Johnson', 'Mathematics', True)
s3 = Student('s103', 'Charlie Lee', 'Physics', True)


while True:
    print('----- Student Management Menu -----')
    print('1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')

    choice = input('Enter your choice (1-4): ')

    if choice == '1':
        s1.view_student_info()
        s2.view_student_info()
        s3.view_student_info()

    elif choice == '2':
        st_id = input('Enter Student id: ')
        st_name = input('Enter Student Name: ')
        st_dept = input('Enter Department: ')

        if st_id == 's101':
            s1.enroll_student(st_id)
        elif st_id == 's102':
            s2.enroll_student(st_id)
        elif st_id == 's103':
            s3.enroll_student(st_id)
        else:
            print('Invalid input')

    elif choice == '3':
        st_id = input('Enter Student id: ')

        if st_id == 's101':
            s1.drop_student()
            print(f'\nStudent {st_id} has been dropped')
        elif st_id == 's102':
            s2.drop_student()
            print(f'\nStudent {st_id} has been dropped')
        elif st_id == 's103':
            s3.drop_student()
            print(f'\nStudent {st_id} has been dropped')
        else:
            print(f'\nInvalid Input')

    elif choice == '4':
        print('\nYou have successfully exited')
        break

    else:
        print('\nInvalid choice')

    print("\n")