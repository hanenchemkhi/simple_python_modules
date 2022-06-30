import pytest
from src.stack_list import Stack
from src.balanced_parentheses import equation_checker

@pytest.fixture
def balanced_equation():
    equation = Stack()
    equation.push("(")
    equation.push("(")
    equation.push("Z")
    equation.push("+")
    equation.push("T")
    equation.push(")")
    equation.push(")")
    return equation

@pytest.fixture
def unbalanced_equation():
    equation = Stack()
    equation.push(")")
    equation.push("(")
    equation.push("Z")
    equation.push("+")
    equation.push("T")
    equation.push(")")
    equation.push(")")
    return equation

def test_balanced_equation_checker(balanced_equation):
    assert equation_checker(balanced_equation) == True

def test_unbalanced_equation_checker(unbalanced_equation):
    assert equation_checker(unbalanced_equation) == False