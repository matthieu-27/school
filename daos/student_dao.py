# -*- coding: utf-8 -*-

"""
Classe Dao[Student]
"""

from models.student import Student
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class StudentDao(Dao[Student]):
    def create(self, student: Student) -> int:
        """Enregistre un étudiant dans la base de données et retourne l'objet complet."""
        with Dao.connection.cursor() as cursor:
            try:
                # 1. Insertion dans la table person
                person_sql = """INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)"""
                person_values = (student.first_name, student.last_name, student.age)
                cursor.execute(person_sql, person_values)
                inserted_id = cursor.lastrowid

                # 3. Insertion dans la table student
                student_sql = "INSERT INTO student (id_person) VALUES (%s)"
                student_values = inserted_id
                cursor.execute(student_sql, student_values)
                Dao.connection.commit()
                return student.student_nbr
            except Exception as e:
                Dao.connection.rollback()
                raise Exception(f"Erreur lors de la création de l'étudiant : {e}")


    def read(self, id_entity: int) -> Optional[Student]:
        """Renvoit l'étudiant correspondant à l'entité dont l'id est id_student
           (ou None s'il n'a pu être trouvé)"""
        student: Optional[Student]
        with Dao.connection.cursor() as cursor:
            sql = """SELECT * FROM student s INNER JOIN person p ON s.id_person = p.id_person WHERE s.student_nbr = %s)"""
            cursor.execute(sql, (id_entity,))
            record = cursor.fetchone()
        if record is not None:
            student = Student(record['first_name'], record['last_name'], record['age'])
            student.student_nbr = record['student_nbr']
        else:
            student = None
        return student


    def fetch_all(self) -> list[Student]:
        """Renvoie un ensemble de tous les étudiants présents en base de données."""
        students = []
        try:
            with Dao.connection.cursor() as cursor:
                sql = """SELECT * FROM student s INNER JOIN person p ON s.id_person = p.id_person """
                cursor.execute(sql)
                records = cursor.fetchall()
                for record in records:
                    if record is not None:
                        student = Student(record['first_name'], record['last_name'], record['age'])
                        student.student_nbr = record['student_nbr']
                        students.append(student)
                    else:
                        student = None
        except Exception as e:
            print(f"Erreur lors de la lecture des étudiants : {e}")
            return list()
        return students


    def update(self, id_entity: int, **fields: Any) -> bool:
        """Met à jour en BD l'entité Student correspondant à id_value, pour y correspondre"""
        if not fields:
            print("Aucun champ à mettre à jour.")
            return False
        with Dao.connection.cursor() as cursor:
            # Construction de la partie SET de la requête
            set_clauses = []
            values = []
            for key, val in fields.items():
                set_clauses.append(f"{key} = %s")
                values.append(val)
            values.append(id_entity)
            sql = (
                    "UPDATE person "
                    "JOIN student ON student.id_person = person.id_person "
                    "SET " + ", ".join(set_clauses) + " "
                                                      "WHERE student.student_nbr = %s"
            )
            try:
                cursor.execute(sql, values)
                Dao.connection.commit()
                print(f"UPDATED COURSE: ROW ID {id_entity}")
            except Exception as e:
                print(f"Erreur lors de la mise à jour des étudiants : {e}")
                return False
            return True


    def delete(self, id_entity: int) -> bool:
        """Supprime en BD l'entité Student correspondant à id_value"""
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM student WHERE id_student=%s"
            try:
                print(f"DELETING COURSE: ROW ID {id_entity}")
                cursor.execute(sql, (id_entity,))
                Dao.connection.commit()
                return True
            except Exception as e:
                Dao.connection.rollback()
                print(f"Erreur lors de la suppression de l'étudiant: {e}")
                return False

