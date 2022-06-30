import pytest
from src.stack_list import Stack
from src.polish_postfix_notation import evaluate_postfix_expression

def test_evaluate_postfix_expression():
    input_list = ["3", "1", "+", "4", "*"]
    assert evaluate_postfix_expression(input) == 16