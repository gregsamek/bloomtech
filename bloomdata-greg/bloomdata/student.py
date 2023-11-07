import random

class Student:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18
    
    def __repr__(self) -> str:
        return f'Student: {self.name}, age: {self.age}'

class BloomTechStudent(Student):

    def __init__(self, name, age, program, current_sprint=0) -> None:
        super().__init__(name, age)
        self.program = program
        self.current_sprint = current_sprint
    
    def advance_to_next_sprint(self):
        self.current_sprint += 1

    def __repr__(self) -> str:
        return f'Student: {self.name}, age: {self.age}, program: {self.program}'

def student_generator():
    names = ('Aaron', 'Bryan', 'Chris', 'David', 'Eric', 'Frank', 'Greg', 
             'Hank', 'Ivan', 'Jake', 'Kyle', 'Luke', 'Mike', 'Nate')
    name = random.choice(names)
    age = random.randint(18, 99)
    programs = ('Data Science', 'Full Stack', 'Backend')
    program = random.choice(programs)
    return BloomTechStudent(name=name, age=age, program=program)

if __name__ == '__main__':
    student_list = []
    for _ in range(30):
        student_list.append(student_generator())
    print(student_list)