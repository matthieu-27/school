# -*- coding: utf-8 -*-

"""
Classe School
"""

from dataclasses import dataclass, field
from typing import Any, Optional

from daos.course_dao import CourseDao
from daos.student_dao import StudentDao
from models.course import Course
from models.teacher import Teacher
from models.student import Student


@dataclass
class School:
    """Couche métier de l'application de gestion d'une école,
    reprenant les cas d'utilisation et les spécifications fonctionnelles :
    - courses : liste des cours existants
    - teachers : liste des enseignants
    - students : liste des élèves"""

    courses: list[Course] = field(default_factory=list, init=False)
    teachers: list[Teacher] = field(default_factory=list, init=False)
    students: list[Student] = field(default_factory=list, init=False)

    def add_course(self, course: Course) -> None:
        """Ajout du cours course à la liste des cours."""
        self.courses.append(course)

    def add_teacher(self, teacher: Teacher) -> None:
        """Ajout de l'enseignant teacher à la liste des enseignants."""
        self.teachers.append(teacher)

    def add_student(self, student: Student) -> None:
        """Ajout de l'élève spécifié à la liste des élèves."""
        self.students.append(student)

    @staticmethod
    def display_courses_list() -> list[Course]:
        """Affichage de la liste des cours avec pour chacun d'eux :
        - leur enseignant
        - la liste des élèves le suivant"""
        course_dao: CourseDao = CourseDao()
        return course_dao.fetch_all()

    @staticmethod
    def get_course_by_id(id_course: int):
        course_dao: CourseDao = CourseDao()
        return course_dao.read(id_course)

    @staticmethod
    def create_course(course: Course):
        course_dao: CourseDao = CourseDao()
        return course_dao.create(course)

    @staticmethod
    def update_course(course_id: int, **fields: Any):
        course_dao: CourseDao = CourseDao()
        return course_dao.update(course_id, **fields)

    @staticmethod
    def delete_course(course_id: int):
        course_dao: CourseDao = CourseDao()
        return course_dao.delete(course_id)

    @staticmethod
    def create_student(student: Student):
        student_dao: StudentDao = StudentDao()
        return student_dao.create(student)

    @staticmethod
    def update_student(student_nbr: int, **fields: Any):
        student_dao: StudentDao = StudentDao()
        return student_dao.update(student_nbr, **fields)

    @staticmethod
    def delete_student(student_id: int):
        student_dao: StudentDao = StudentDao()
        return student_dao.delete(student_id)

    @staticmethod
    def get_student_by_id(student_id: int):
        student_dao: StudentDao = StudentDao()
        return student_dao.read(student_id)

    @staticmethod
    def display_student_list() -> list[Student]:
        """Affichage de la liste des élèves"""
        student_dao: StudentDao = StudentDao()
        return student_dao.fetch_all()
