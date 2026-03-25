class Student:
    def __init__(self, nom, Archi_appli, Monitoring, Integr_Continue):
        self.nom = nom
        self.Archi_appli = Archi_appli
        self.Monitoring = Monitoring
        self.Integr_Continue = Integr_Continue

    def __repr__(self):
        return f"Student({self.nom}, {self.Archi_appli}, {self.Monitoring}, {self.Integr_Continue})"

class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)