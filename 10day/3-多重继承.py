class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class Skills(object):
    pass

class BasketballSkill(Skills):
    def skill(self):
        return 'basketball'

class FootballSkill(Skills):
    def skill(self):
        return 'football'

class BStudent(Student, BasketballSkill):
    pass

class FTeacher(Teacher, FootballSkill):
    pass

s = BStudent()
print (s.skill())

t = FTeacher()
print (t.skill())
