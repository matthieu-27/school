from business.school import School

if __name__ == "__main__":
    print("""\
    --------------------------
    Bienvenue dans notre école
    --------------------------""")

    school: School = School()

    # affichage de la liste des cours, leur enseignant et leurs élèves
    for course in school.display_courses_list(school):
        print(course)
