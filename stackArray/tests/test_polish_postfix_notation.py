import pytest

from src.polish_postfix_notation import evaluate_postfix_expression


@pytest.fixture
def input_list():
    return ["3", "1", "+", "4", "*"]

def test_evaluate_postfix_expression(input_list):
    assert evaluate_postfix_expression(input_list) == '16'

