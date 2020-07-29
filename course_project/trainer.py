from person import Person

class Trainer(Person):
    def __init__(self, id, firstName, lastName, phoneNumber, dateOfBirth, domain, salary):
        super().__init__(firstName, lastName, phoneNumber, dateOfBirth)
        self.id = id
        self.domain = domain
        self.salary = salary
        self.courses = []
        self.got_raise = False

    def __repr__(self):
        return f"Trainer '{self.id}': {self.firstName} {self.lastName} - {self.domain} - {self.salary}"

    def check_for_raise(self):
        if len(self.courses) >=4 and not self.got_raise:
            self.salary += 10000
            self.got_raise = True

    def add_course(self, course):
        from course import Course
        if not isinstance(course, Course):
            raise Error('Invalid Course')
        else:
            self.courses.append(course)

    def convert_courses_into_string(self):
        if len(self.courses) != 0:
            str_courses = ''
            counter = 0
            for course in self.courses:
                str_ = course.name + ' ' + course.code + ';'
                str_courses += str_
                counter +1

            return str_courses
