from business.school import School
from daos.student_dao import StudentDao
from models.course import Course
from datetime import date

from models.student import Student

if __name__ == "__main__":
    print("""\
    --------------------------
    Bienvenue dans notre école
    --------------------------""")

    school: School = School()

    # svt: Course = Course("SVT", date(2024, 3, 4),
    #                        date(2024, 3, 15))
    #
    # school.delete_course(school.create_course(svt))


    school.update_student(33, last_name="Malu", age=13)
