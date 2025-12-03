from business.school import School
from models.course import Course
from datetime import date

if __name__ == "__main__":
    print("""\
    --------------------------
    Bienvenue dans notre école
    --------------------------""")

    school: School = School()

    svt: Course = Course("SVT", date(2024, 3, 4),
                           date(2024, 3, 15))
    school.create_course(svt)
    # affichage de la liste des cours, leur enseignant et leurs élèves
    for course in school.display_courses_list(school):
        print(course)