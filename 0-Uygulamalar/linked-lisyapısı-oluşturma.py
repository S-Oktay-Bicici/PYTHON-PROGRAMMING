# ### Linked List Yapısı oluşturun
# ### [4|c] ---> [8|b] ---> [3|a] ---> [1|None]

class Node:
    
    def __init__(self, data, next=None):
        self.Data = data
        self.Next = next
        
    def get_data(self):
        return self.Data
    
    def next(self):
        return self.Next

a = Node(1)
b = Node(3, a)
c = Node(8, b)
d = Node(4, c)

