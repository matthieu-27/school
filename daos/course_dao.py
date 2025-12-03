# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from models.course import Course
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> None:
        """ Enregistre un cours dans la base de données et indique un message de succès."""
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO course (name, start_date, end_date, id_teacher) VALUES (%s, %s, %s, %s)"
            values = (course.name, course.start_date, course.end_date, 1)
            cursor.execute(sql, values)
            Dao.connection.commit()
            print(f"INSERTED COURSE: ROW ID {cursor.lastrowid}")

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        course: Optional[Course]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM course WHERE id_course=%s"
            cursor.execute(sql, (id_course,))
            record = cursor.fetchone()
        course = CourseDao.get_data(record)

        if course:
            return course
        else:
            return None

    @staticmethod
    def get_data(record: tuple[Any, ...] | None) -> Course | None:
        if record is not None:
            course = Course(record['name'], record['start_date'], record['end_date'])
            course.id = record['id_course']
            # course.teacher = record['id_teacher'] TODO : IMPLEMENT DAO
            return course
        return None

    def read_all(self) -> Optional[list[Course]]:
        """Renvoie un ensemble de tous les cours présents en base de données."""
        courses = []
        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM course"
                cursor.execute(sql)
                records = cursor.fetchall()
            for rec in records:
                course = self.get_data(rec)
                if course:
                    courses.append(course)
        except Exception as e:
            print(f"Erreur lors de la lecture des cours : {e}")
            return None
        return courses

    def update(self, id_value: int, **fields: Any) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre"""
        with Dao.connection.cursor() as cursor:
            query = ""
            count = 1
            for key, val in fields.items():
                query += f"{key} = '{str(val)}'{", " if len(fields) != count else ""}"
                count += 1
            sql = ("UPDATE course SET "
                   + query +
                   f" WHERE id_course={id_value}")
            print(sql)
            try:
                cursor.execute(sql)
                Dao.connection.commit()
                print(f"UPDATED COURSE: ROW ID {id_value}")
            except Exception as e:
                print(f"Erreur lors de la mise à jour des cours : {e}")
                return False
            return True

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
