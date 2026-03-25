class Student:
    def __init__(self, nom, Archi_appli, Monitoring, Integr_Continue):
        self.nom = nom
        self.Archi_appli = Archi_appli
        self.Monitoring = Monitoring
        self.Integr_Continue = Integr_Continue

    def __repr__(self):
        return f"Student({self.nom}, {self.Archi_appli}, {self.Monitoring}, {self.Integr_Continue})"

class Class:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def rank_matter_1(self):
        return sorted(self.students, key=lambda s: s.Archi_appli, reverse=True)

if __name__ == '__main__':
    school_class = Class()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print(school_class.rank_matter_1())



