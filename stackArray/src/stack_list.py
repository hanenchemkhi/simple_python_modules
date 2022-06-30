"""
Creates a Stack using linked-list 
"""
class Node :
    def __init__(self, data = None, prev = None):
        self.data = data 
        self.prev = prev

class Stack:
    def __init__(self):
        self.tail = None
    
    def push(self, data):
        new_node = Node(data)
        if self.tail :
            current = self.tail
            self.tail = new_node
            new_node.prev = current
        else :
            self.tail = new_node
    
    def peek(self):
        if self.tail:
            return self.tail.data
        else : 
            return None

    def pop(self):
        try :
            if not self.tail :
                raise Exception ("Stack is empty")
            value=self.tail.data
            self.tail = self.tail.prev
            return value
        except Exception as e :
            print(e)
        



