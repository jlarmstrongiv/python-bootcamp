class Student:
  def __init__(self, name, cuid, grade):
    self.name = name
    self.cuid = cuid
    self.grade = grade
    self.needs_orange_juice = True

  university = 'Clemson'

  def say_hello(self):
    print(f'{self.name} says hi')

class ResearchGroup:
  def __init__(self, groupname, students):
    self.groupname = groupname
    self.students = students

  def group_greeting(self):
    for student in self.students:
      student.say_hello()


Jake = Student('Jake from State Farm', 'C20498951', 'Senior')
Jake.university

Rui = Student('Rui', '123094', 'Grad Student')
Rui.needs_orange_juice = False
Rui.university

trace_students = [Jake, Rui]

TraceGroup = ResearchGroup('Trace', trace_students)

TraceGroup.students

TraceGroup.group_greeting()
