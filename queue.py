class Queue:
    def __init__(self):
        self.data = []
        self.front = 0
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return 'Queue is empty'
        else:
            return False
    
    def enqueue(self, element):
        self.data.append(element)
        self.size = self.size + 1
    
    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            value = self.data[self.front]
            self.data[self.front] = None
            self.front = self.front + 1
            self.size = self.size - 1
            return value
    
    def first(self):
        if self.is_empty():
            return 'Queue is Empty'
        else:
            return self.data[self.front]


q = Queue()
q.enqueue(10)
q.enqueue(20)
print('Queue :', q.data)
print('Is - Empty :', q.is_empty())
print('Length:', len(q))
print('Popped:', q.dequeue())
print('Popped:', q.dequeue())
print('Is - Empty :', q.is_empty())
print('Popped:', q.dequeue())
print('First:', q.first())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print('Queue: ', q.data)
print('First:', q.first())