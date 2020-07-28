from datetime import datetime

class Enrollment():
        def __init__(self, employee, course):
            from employee import Employee
            if not isinstance(employee, Employee):
                raise Error('Invalid employee!')

            from course import Course
            if not isinstance(course, Course):
                raise Error('Invalid course!')

            self.employee = employee
            self.course = course
            self.grade = None
            self.date = datetime.now()

        def __repr__(self):
            return f"Enrolment: {self.employee.firstName} {self.employee.lastName} - {self.course.code}: {self.course.trainers}"

        def set_grade(self, grade):
            self.grade = grade
