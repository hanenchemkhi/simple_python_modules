import pytest
from src.stack_list import Stack

@pytest.fixture
def empty_stack():
    stack= Stack()
    return stack

@pytest.fixture
def stack():
    stack= Stack()
    stack.push("Hello")
    stack.push(100)
    return stack


def test_peek_empty_stack(empty_stack):
    assert empty_stack.peek()== None

def test_pop_empty_stack(empty_stack):
    with pytest.raises(Exception) as e:
        empty_stack.pop()
        assert e.type == Exception

def test_push_empty_stack(empty_stack):
    empty_stack.push(12)
    assert empty_stack.peek() == 12

def test_peek_not_empty_stack(stack):
    stack.push(10)
    stack.push("Hello")
    assert stack.peek()=="Hello"


def test_pop_not_empty_stack(stack):
    stack.push(10)
    stack.push("Hello")
    assert stack.pop()=="Hello"

def test_push_stack(stack):
    stack.push(50)
    stack.push("Hello")
    assert stack.peek()=="Hello"
    

