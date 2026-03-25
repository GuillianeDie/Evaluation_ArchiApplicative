from collections.abc import Iterable, Iterator

def ajout_4_matiere(cls):
    orig_init = cls.__init__
    def __init__(self, nom, Archi_appli, Monitoring, Integr_Continue, matiere_4=0):
        orig_init(self, nom, Archi_appli, Monitoring, Integr_Continue)
        self.matiere_4 = matiere_4
    cls.__init__ = __init__
    return cls

def ajout_4_matiere_iterator(cls):
    class MatterIterator_4(Iterator):
        def __init__(self, students):
            self._students = sorted(students, key=lambda s: s.matiere_4, reverse=True)
            self._index = 0
        def __next__(self):
            if self._index < len(self._students):
                res = self._students[self._index]
                self._index += 1
                return res
            raise StopIteration
    cls.get_matiere_4 = lambda self: MatterIterator_4(self.students)
    return cls

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

@ajout_4_matiere
class Student:
    def __init__(self, nom, Archi_appli, Monitoring, Integr_Continue):
        self.nom = nom
        self.Archi_appli = Archi_appli
        self.Monitoring = Monitoring
        self.Integr_Continue = Integr_Continue

    def __repr__(self):
        return f"Student({self.nom}, {self.Archi_appli}, {self.Monitoring}, {self.Integr_Continue}, {self.matiere_4})"

class MatterIterator_Archi_appli(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.Archi_appli, reverse=True)
        self._index = 0
    def __next__(self):
        if self._index < len(self._students):
            res = self._students[self._index]
            self._index += 1
            return res
        raise StopIteration
    
class MatterIterator_Monitoring(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.Monitoring, reverse=True)
        self._index = 0
    def __next__(self):
        if self._index < len(self._students):
            res = self._students[self._index]
            self._index += 1
            return res
        raise StopIteration
    
class MatterIterator_Integr_Continue(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.Integr_Continue, reverse=True)
        self._index = 0
    def __next__(self):
        if self._index < len(self._students):
            res = self._students[self._index]
            self._index += 1
            return res
        raise StopIteration

@ajout_4_matiere_iterator
class Class(Iterable, metaclass=Singleton):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return MatterIterator_Archi_appli(self.students)
    
    def get_Monitoring(self):
        return MatterIterator_Monitoring(self.students)
    
    def get_Integr_Continue(self):
        return MatterIterator_Integr_Continue(self.students)

if __name__ == '__main__':
    school_class = Class()
    school_class.add_student(Student('J', 10, 12, 13, 18))
    school_class.add_student(Student('A', 8, 2, 17, 5))
    school_class.add_student(Student('V', 9, 14, 14, 12))

    other_class = Class()
    print(school_class is other_class)

    for student in school_class:
        print(student)
    for student in school_class.get_Monitoring():
        print(student)
    for student in school_class.get_Integr_Continue():
        print(student)
    for student in school_class.get_matiere_4():
        print(student)