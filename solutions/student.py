class Student:
    def __init__(self, name : str):
        self.name = name
        self._grades = {}

    def add_grade(self, subject, grade):
        if not (isinstance(grade, int) and 2 <= grade <= 5):
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self._grades.setdefault(subject, []).append(grade)

    def average(self, subject=None):
        if subject is None:
            all_grades = [g for grades in self._grades.values() for g in grades]
            if not all_grades:
                return 0
            return sum(all_grades) / len(all_grades)
        if subject not in self._grades:
            raise KeyError(f"Нет оценок по предмету {subject}")
        grades = self._grades[subject]
        return sum(grades) / len(grades)

    def subjects(self):
        return sorted(self._grades)

    def debts(self):
        result = []
        for subject in sorted(self._grades):
            grades = self._grades[subject]
            if sum(grades) / len(grades) < 3:
                result.append(subject)
        return result

    def __lt__(self, other):
        return self.average() < other.average()

    def __repr__(self):
        return f"Student('{self.name}', {self.average():.2f})"
    
class Group:
    def __init__(self, name: str):
        self.name = name
        self._students = []

    def add(self, student):
        if not isinstance(student, Student):
            raise TypeError("Можно добавлять только студентов")
        if any(s.name == student.name for s in self._students):
            raise ValueError(f"Студент с именем {student.name} уже есть")
        self._students.append(student)

    def __len__(self):
        return len(self._students)
    
    def __contains__(self, name):
        return any(s.name == name for s in self._students)

    def ranking(self):
        return sorted(self._students, key=lambda s: (-s.average(), s.name))

    def with_debts(self):
        return sorted(s.name for s in self._students if s.debts())