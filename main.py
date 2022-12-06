class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'фамилия: {self.surname}'
        return res


student1 = Student('Ruoy', 'Eman', 'female')
student1.courses_in_progress += ['Python', 'Java']
student1.finished_courses +=['Введение в програмирование', 'Git']

student2 = Student('Ivan', 'Post', 'male')
student2.courses_in_progress += ['Java', 'Git']
student2.finished_courses +=['Введение в програмирование', 'Python']

student3 = Student('Ira', 'Blok', 'female')
student3.courses_in_progress += ['Python', 'Java', 'Git']
student3.finished_courses +=['Введение в програмирование']


reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python', 'Java']

reviewer2 = Reviewer('Koli', 'Gudman')
reviewer2.courses_attached += ['Java']

reviewer3 = Reviewer('Sili', 'Terok')
reviewer3.courses_attached += ['Git', 'Java']


lecturer1 = Lecturer('Pol', 'Rif')
lecturer1.courses_attached += ['Java', 'Python']

lecturer2 = Lecturer('Billi', 'Hupper')
lecturer2.courses_attached += ['Git', 'Java']

lecturer3 = Lecturer('Vera', 'Tenet')
lecturer3.courses_attached += ['Python', 'Java']


reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Java', 7)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Java', 8)

reviewer3.rate_hw(student2, 'Git', 9)
reviewer3.rate_hw(student2, 'Java', 8)
reviewer3.rate_hw(student2, 'Git', 10)
reviewer2.rate_hw(student2, 'Java', 6)

reviewer1.rate_hw(student3, 'Python', 6)
reviewer1.rate_hw(student3, 'Java', 10)
reviewer1.rate_hw(student3, 'Python', 7)
reviewer2.rate_hw(student3, 'Java', 8)
reviewer3.rate_hw(student3, 'Git', 4)
reviewer3.rate_hw(student3, 'Git', 6)


student1.rate_hw(lecturer1, 'Python', 9)
student1.rate_hw(lecturer1, 'Java', 8)
student2.rate_hw(lecturer1, 'Java', 5)
student3.rate_hw(lecturer1, 'Java', 8)
student3.rate_hw(lecturer1, 'Python', 4)

student1.rate_hw(lecturer2, 'Java', 6)
student2.rate_hw(lecturer2, 'Java', 5)
student2.rate_hw(lecturer2, 'Git', 9)
student3.rate_hw(lecturer2, 'Git', 8)
student3.rate_hw(lecturer2, 'Java', 7)

student1.rate_hw(lecturer3, 'Java', 5)
student2.rate_hw(lecturer3, 'Java', 8)
student1.rate_hw(lecturer3, 'Python', 10)
student3.rate_hw(lecturer3, 'Python', 7)
student3.rate_hw(lecturer3, 'Java', 10)


print(f'Список студентов:\n{student1}\n\n{student2}\n\n{student3}\n')
print(f'Список лекторов:\n{lecturer1}\n\n{lecturer2}\n\n{lecturer3}\n')
print(f'Список экспертов:\n{reviewer1}\n\n{reviewer2}\n\n{reviewer3}\n')
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student1.name} {student1.surname} < {student2.name} {student2.surname} = {student1 < student2}')
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student1.name} {student1.surname} < {student3.name} {student3.surname} = {student1 < student3}')
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student3.name} {student3.surname} < {student2.name} {student2.surname} = {student3 < student2}')
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{lecturer1.name} {lecturer1.surname} < {lecturer2.name} {lecturer2.surname} = {lecturer1 < lecturer2}')
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{lecturer1.name} {lecturer1.surname} < {lecturer3.name} {lecturer3.surname} = {lecturer1 < lecturer3}')
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{lecturer3.name} {lecturer3.surname} < {lecturer2.name} {lecturer2.surname} = {lecturer3 < lecturer2}')

lecturer_list = [lecturer1, lecturer2, lecturer3]
student_list = [student1, student2, student3]


def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for student in student_list:
       if course_name in student.courses_in_progress:
            sum_all += student.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lecturer in lecturer_list:
        if course_name in lecturer.courses_attached:
            sum_all += lecturer.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"\nСредняя оценка для всех студентов по курсу Java: {student_rating(student_list, 'Java')}")
print(f"\nСредняя оценка для всех лекторов по курсу Java: {lecturer_rating(lecturer_list, 'Java')}")
