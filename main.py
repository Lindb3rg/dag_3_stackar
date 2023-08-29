

# Stack

class Stack:

    def __init__(self):
        self.stack_of_elements = []
        self.STACK_LIMIT = 5
        self.element_counter = 0


    def check_stack_limit(self):
        if self.element_counter < self.STACK_LIMIT:
            return True
        return False
    
    def push(self, new_element):
        if self.check_stack_limit():
            self.stack_of_elements.append(new_element)
            self.element_counter += 1
            return
        return print("Stack is full!")
        
    def peek(self):
        return print(f"{self.stack_of_elements[-1]}")
        

    def is_full(self):
        if len(self.stack_of_elements) == 0:
            return print("Stack is full!")
        return print(f"{10 - len(self.stack_of_elements)} stacks left." )


    def pop(self):
        if self.check_stack_limit():
            self.element_counter -= 1
            return self.stack_of_elements.pop()
    

    def is_empty(self):
        if len(self.stack_of_elements == 0):
            return print("Stack is empty")
    

class Queue:

    def __init__(self):
        self.stack_of_elements = []
        self.STACK_LIMIT = 5
        self.element_counter = 0


    def check_stack_limit(self):
        if self.element_counter < self.STACK_LIMIT:
            return True
        return False
    
    def push(self, new_element):
        if self.check_stack_limit():
            self.stack_of_elements.append(new_element)
            self.element_counter += 1
            return
        return print("Stack is full!")
        
    def peek(self):
        return print(f"{self.stack_of_elements[-1]}")
        

    def is_full(self):
        if len(self.stack_of_elements) == 0:
            return print("Stack is full!")
        return print(f"{10 - len(self.stack_of_elements)} stacks left." )


    def pop(self):
        if self.check_stack_limit():
            self.element_counter -= 1
            return self.stack_of_elements.pop(0)
    

    def is_empty(self):
        if len(self.stack_of_elements == 0):
            return print("Stack is empty")











if __name__ == "__main__":


    stack = Stack()

    stack.push(1)
    stack.push(4)
    stack.push(3)
    stack.pop()
    stack.push(3)
    stack.push(1)
    stack.peek()
    stack.is_full()
    stack.push(1)

    
    



