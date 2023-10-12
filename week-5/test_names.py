"""

Team: 3 (Tristan Galloway, Jude Ebigide)
Teacher: Brother Clements
File: test_names.py
Purpose: Writing and running test functions often help a software 
developer find mistakes in code. During this assignment, you will 
write three test functions. Then use pytest to run the test functions
and use the output of pytest to help you find and fix errors in some 
program functions.

"""

from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():

    assert make_full_name("Tristan", "Galloway") == "Galloway; Tristan"
    assert make_full_name("Karli", "Williams") == "Williams; Karli"
    assert make_full_name("Ben", "Zenger") == "Zenger; Ben"

def test_extract_family_name():

    assert extract_family_name("Galloway; Tristan") == "Galloway"
    assert extract_family_name("Williams; Karli") == "Williams"
    assert extract_family_name("Zenger; Ben") == "Zenger"

def test_extract_given_name():

    assert extract_given_name("Galloway; Tristan") == "Tristan"
    assert extract_given_name("Williams; Karli") == "Karli"
    assert extract_given_name("Zenger; Ben") == "Ben"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])