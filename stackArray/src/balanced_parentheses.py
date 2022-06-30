from src.stack_list import Stack
"""
    Check equation for balanced parentheses

    Args:
       equation(linked list): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
"""

def equation_checker(equation):
    paren = []
    while  equation.peek()!= None :
        popped = equation.pop()
        if popped == ")":
            paren.append(popped)
        elif popped == "(":
            if paren[len(paren)-1]==")" :
                paren.pop()
            
        continue
    if paren == None :
        return True
    else :
        return False 
