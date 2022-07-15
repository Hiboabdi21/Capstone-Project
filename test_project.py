import pytest
import project

# Testcase for checking Invalid Email
def test_getEmail1():
   assert project.getEmail("@testWrongEmail") == "Invalid Email"

# Testcase for checking valid Email
def test_getEmail2():
   assert project.getEmail("testCorrectmail@gmail.com") == "testCorrectmail@gmail.com"

# Testcase for checking Invalid Password
def test_getPassword1():
   assert project.getPassword("123") == "Invalid Password"

# Testcase for checking valid Email
def test_getPassword2():
   assert project.getPassword("test1234") == "test1234"