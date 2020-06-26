class Dequeue():
    def __init__(self):
        self.data = []
        self.front = 0

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        if len(self.data) == 0:
            return 'Empty'
        else:
            False
    
    def first(self):
        if self.is_empty():
            return 'Empty'
        else:
            return self.data[self.front]
        
    def add_first(self, element):
        slef.data.insert(self.front, element)
    
    def add_last(self, element):
        self.data.append(element)
    
    def delete_first(self):
        if self.is_empty():
            return 'Empty'
        else:
            value = self.data.pop(self.front)
            return value
    
    def delete_last(self):
        if self.is_empty():
            return 'Empty'
        else:
            return self.data.pop()
        

d = Dequeue()
d.add_last(10)
d.add_last(20)
d.add_last(30)
d.add_last(40)
print('Dequeue: ',d.data)
print('Lenght: ', len(d))
print('Is empty: ', d.is_empty())
print('Delete from last: ', d.delete_last())
print('Dequeue: ', d.data)
print('Delete from first: ', d.delete_first())
print('Dequeue: ', d.data)
print('Is empty: ', d.is_empty())
print('Delete from last: ', d.delete_last())
print('Delete from last: ', d.delete_last())
print('Dequeue: ', d.data)
print('Is empty: ', d.is_empty())
print('Lenght: ', len(d))