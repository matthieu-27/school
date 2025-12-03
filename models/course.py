# -*- coding: utf-8 -*-

"""
Classe Course
"""

# pour simplifier les annotations de types des classes non importées à l'exécution
# (teacher: Teacher plutôt que teacher: 'Teacher')
from __future__ import annotations

from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass, field
from datetime import date

# pour éviter une circularité des imports à l'exécution,
# les classes Student et Teacher important la classe Course
if TYPE_CHECKING:
    from .student import Student
    from .teacher import Teacher


@dataclass
class Course:
    """Cours enseigné à l'école :
    - id                 : clé primaire de l'entité persistante
    - name               : nom du cours
    - start_date         : date de début
    - end_date           : date de fin
    - teacher            : enseignant de ce cours
    - students_taking_it : élèves qui suivent ce cours
    """
    id: Optional[int] = field(default=None, init=False)
    name: str
    start_date: date
    end_date: date
    teacher: Optional[Teacher] = field(default=None, init=False)
    students_taking_it: list[Student] = field(default_factory=list, init=False)

    def __str__(self) -> str:
        course_str = f"{self.name} ({self.start_date} – {self.end_date}),\n"
        course_str += f"enseigné par {self.teacher}" \
            if self.teacher is not None else "pas d'enseignant affecté"
        return course_str

