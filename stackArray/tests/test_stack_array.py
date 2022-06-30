
import pytest 
from src.stack_array import Stack

@pytest.fixture
def empty_stack():
    stack_arr = Stack()
    return stack_arr

@pytest.fixture
def full_stack():
    stack_arr = Stack()
    stack_arr.arr_index = 10
    stack_arr.arr = [10 for _ in range(10)]
    return stack_arr

@pytest.fixture
def not_empty_stack():
    stack_arr = Stack()
    stack_arr.arr_index = 3
    stack_arr.arr = [5,20,10]
    return stack_arr

def test_top_empty_stack(empty_stack):
    assert empty_stack.top()== None

def test_pop_empty_stack(empty_stack):
    assert empty_stack.pop() == None

def test_pop_not_empty_stack(not_empty_stack):
    assert not_empty_stack.pop()!= None

def test_pop_not_empty_stack(not_empty_stack):
    assert not_empty_stack.pop() != None

def test_pop_empty_stack(empty_stack):
    assert empty_stack.pop() == None

def test_push_to_full_stack(full_stack):
    with pytest.raises(Exception) as e:
        full_stack.push(10) 
        assert e.type == IndexError
    

def test_push_to_empty_stack(empty_stack):
    empty_stack.push(100)
    assert empty_stack.arr[empty_stack.arr_index-1] == 100

def test_size_for_not_empty_stack(not_empty_stack):
    assert not_empty_stack.size()== 3
    
def test_size_for_empty_stack(empty_stack):
    assert empty_stack.size() == 0

def test_is_empty(empty_stack, not_empty_stack):
    assert empty_stack.is_empty() is True
    assert not_empty_stack.is_empty() is False

def test_is_full(empty_stack, full_stack) :
    assert empty_stack.is_full() is False
    assert full_stack.is_full() is True

    """
    To run the test:
    python setup.py develop
    python -m pip install pytest
    pytest    
    python -m pip install pytest-cov
    pytest --cov src --cov-report html
    """