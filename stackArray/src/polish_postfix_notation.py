from src.stack_list import Stack

"""
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
 """
def evaluate_postfix_expression(input_list):
   stack = Stack()

   for element in input_list :
      if element in ["+", "-", "*", "/"] :
         operand_1 = stack.pop()
         operand_2 = stack.pop()
         result = int(eval(operand_1 +element+operand_2))
         stack.push(str(result))
      else :
         stack.push(element)
   
   return stack.pop()