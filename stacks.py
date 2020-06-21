class Stack() :
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.is_empty() :
            return 'Stack is empty'
        else:
            return self.data.pop()
    
    def top(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            return self.data[-1]

s = Stack()
s.push(10)
s.push(20)
print('Stack :', s.data)
print('Is - Empty :', s.is_empty())
print('Length:', len(s))
print('Popped:', s.pop())
print('Popped:', s.pop())
print('Is - Empty :', s.is_empty())
print('Popped:', s.pop())
print('Top:', s.top())
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print('Stack: ', s.data)
print('TOP:', s.top())