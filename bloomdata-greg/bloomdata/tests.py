import pytest
import bloomdata.student as Student

@pytest.fixture
def bt_student():
    return Student.BloomTechStudent(name='Adam', age=30, program='Data Science')

def test_bt_student_name(bt_student):
    assert bt_student.name == 'Adam'

def test_bt_student_age(bt_student):
    assert bt_student.age == 30

def test_bt_student_program(bt_student):
    assert bt_student.program == 'Data Science'

def test_advance_to_next_sprint(bt_student):
    bt_student.advance_to_next_sprint()
    assert bt_student.current_sprint == 1