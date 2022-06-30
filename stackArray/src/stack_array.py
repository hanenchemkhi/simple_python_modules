
from logging import raiseExceptions


class Stack :
    def __init__(self, default_size= 10):
        self.arr = [None for _ in range (default_size)]
        self.arr_index = 0
    
    def top(self):
        return self.arr[self.arr_index - 1]

    def pop(self):
        self.arr_index-= 1
        return self.arr[self.arr_index]
    
    def push(self, element):  
        try :      
            self.arr[self.arr_index] = element
            self.arr_index += 1
            return True
        except IndexError :
            print("You've already reached the end of your stack")
            return False

    def size(self):
        return self.arr_index

    def is_empty(self):
        if self.arr_index== 0:
            return True
        return False

    def is_full(self):
        if len(self.arr)> self.arr_index :
            return False
        return True


stack = Stack()
for i in range (100):
    if not stack.push(i) :
        break
print(stack.arr_index)

