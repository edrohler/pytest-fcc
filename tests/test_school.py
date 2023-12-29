import pytest
from source.school import ClassRoom, Teacher, Student, TooManyStudentsError

# Harry Potter themed fixtures
@pytest.fixture
def dumbledore():
    return Teacher("Albus Dumbledore")

@pytest.fixture
def students():
    return [Student(f"Student {i}") for i in range(15)]

@pytest.fixture
def classroom(dumbledore, students):
    return ClassRoom(dumbledore, students, "Defense Against the Dark Arts")

# Test initialization of ClassRoom
def test_classroom_init(classroom):
    assert classroom.teacher.name == "Albus Dumbledore"
    assert len(classroom.students) == 15
    assert classroom.course_title == "Defense Against the Dark Arts"

# Test adding a student
def test_add_student(classroom):
    harry = Student("Harry Potter")
    classroom.add_student(harry)
    assert harry in classroom.students

# Test adding too many students
def test_add_too_many_students(classroom):
    for i in range(5):
        classroom.add_student(Student(f"Extra Student {i}"))
    assert len(classroom.students) == 20
    with pytest.raises(TooManyStudentsError):
        classroom.add_student(Student("One Too Many"))


# Test removing a student
def test_remove_student(classroom):
    student_to_remove = classroom.students[0]
    classroom.remove_student(student_to_remove)
    assert student_to_remove not in classroom.students

# Test removing a student not in class
def test_remove_student_not_in_class(classroom):
    random_student = Student("Random Student")
    original_count = len(classroom.students)
    classroom.remove_student(random_student)
    assert len(classroom.students) == original_count

# Test changing the teacher
def test_change_teacher(classroom):
    snape = Teacher("Severus Snape")
    classroom.change_teacher(snape)
    assert classroom.teacher.name == "Severus Snape"
