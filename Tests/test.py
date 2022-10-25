import pytest
import System


# The original function takes a name and password and sets the user for the program. Verify that the correct user is created with this test, and use
# the json files to check that it adds the correct data to the user. This test should PASS.
def test_login(gradingSystem):
    user = "5678"
    passw = "abcd"
    gradingSystem.login(user, passw)
    if (user in gradingSystem.users):
        assert True
    else:
        assert False
    
    

# The original function checks that the password is correct. Enter several different formats of passwords to verify that the password returns correctly if the
# passwords are the same. This test should PASS.
def test_check_password(gradingSystem):
    user = "goggins"
    wrong_password1 = "46"
    wrong_password2 = "bye"
    correct_password = "augurrox"
    test1 = gradingSystem.check_password(user, wrong_password1)
    test2 = gradingSystem.check_password(user, wrong_password2)
    test3 = gradingSystem.check_password(user, correct_password)
    if (test1 == test2 == test3):
        assert False
    else:
        assert True
        

# The original function will change the grade of a student and updates the database. Verify that the correct grade is changed on the correct user in the
# database. This test should FAIL.
def test_change_grade(gradingSystem):
    gradingSystem.login('cmhbf5', 'bestTA')
    coursename = "cloud_computing"
    gradingSystem.usr.change_grade("yted91",coursename, "assignment2", 0)
    gradingSystem.reload_data()
    grade_in_database = gradingSystem.users["yted91"]["courses"][coursename]["assignment2"]["Grade"]

    if (grade_in_database != 0):
        assert False
    else:
        assert True

    

# The original function allows the staff to create a new assignment. Verify that an assignment is created with the correct due date in the correct course in
# the database. This test should FAIL.
def test_create_assignment(gradingSystem):
    gradingSystem.login('cmhbf5', 'bestTA')
    coursename = "databases"
    gradingSystem.usr.create_assignment("ABCD", "1/1/20", "databases")
    gradingSystem.reload_data()
    assignment = gradingSystem.courses["databases"]["assignments"]["assignment2"]
    due_date = assignment["due_date"]
    if ( (due_date == "1/1/20" and assignment) and (gradingSystem.courses["databases"]["ta"] == "cmhbf5")):
        assert True
    else:
        assert False

    

# The original function allows the professor to add a student to a course. Verify that a student will be added to the correct course in the database.
# This test should FAIL.
def test_add_student(gradingSystem):
    gradingSystem.login('goggins', 'augurrox')
    coursename = "databases"
    gradingSystem.usr.add_student("yted91", coursename)
    gradingSystem.reload_data()
    if ("databases" in gradingSystem.users["yted91"]["courses"]):
        assert True
    else:
        assert False

# The original function allows the professor to drop a student in a course. Verify that the student is added and dropped from the correct course in the# database. 
# This test should FAIL.
def test_drop_student(gradingSystem):
    gradingSystem.login('goggins', 'augurrox')
    coursename = "databases"
    gradingSystem.usr.drop_student("yted91", "databases")
    gradingSystem.reload_data()
    if ("databases" in gradingSystem.users["yted91"]["courses"]):
        assert False
    else:
        assert True
    
    

# The original function allows a student to submit an assignment. Verify that the database is updated with the correct assignment, submission,
# submission date and in the correct course. This test should PASS.
def test_submit_assignment(gradingSystem):
    gradingSystem.login('hdjsr7', 'pass1234')
    gradingSystem.usr.submit_assignment("software_engineering","assignment7","Blah Blah","2/3/20")
    gradingSystem.reload_data()
    if (gradingSystem.courses["software_engineering"]["assignment7"]):
        assert True
    else
        assert False

    
# The original function checks if an assignment is submitted on time. Verify that it will return true if the assignment is on time, and false if the assignment
# is late. This test should PASS.
def test_check_ontime(gradingSystem):
    gradingSystem.login('hdjsr7', 'pass1234')
    submission_date = gradingSystem.users["hdjsr7"]["courses"]["databases"]["assignment2"]["submission_date"]
    due_date = gradingSystem.courses["databases"]["assignments"]["assignment2"]["due_date"]
    if (gradingSystem.usr.check_ontime(submission_date,due_date) == True):
        assert True
    else:
        assert False
    
    

# The original function returns the users grades for a specific course. Verify the correct grades are returned for the correct user.
# this test should FAIL.
def test_check_grades(gradingSystem):
    gradingSystem.login('yted91', "imoutofpasswordnames")
    coursename = "cloud_computing"
    correct_assignments = gradingSystem.courses[coursename]["assignments"]
    test_assignments = gradingSystem.usr.check_grades(coursename)
    correct_assignment1 = correct_assignments["assignment1"]
    test_assignment1 = test_assignments[0]
    if (correct_assignment1 == test_assignment1):
        assert True
    else:
        assert False
                                        

# The original function returns assignments and their due dates for a specific course. Verify that the correct assignments for the correct course are
# returned. This test should PASS.
def test_view_assignments(gradingSystem):
    coursename = "databases"
    gradingSystem.login('hdjsr7', 'pass1234')
    correct_assignments = gradingSystem.courses[coursename]["assignments"]
    test_assignments = gradingSystem.usr.view_assignments("databases")
    if (correct_assignments == test_assignments):
        assert True
    else:
        assert False
    

#@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
