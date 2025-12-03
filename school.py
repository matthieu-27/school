from business.school import School

if __name__ == "__main__":
    print("""\
    --------------------------
    Bienvenue dans notre école
    --------------------------""")

    school: School = School()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    school.init_static()

    # affichage de la liste des cours, leur enseignant et leurs élèves
    school.display_courses_list()

    print(school.get_course_by_id(1))
