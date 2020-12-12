# ### Stack yapısını implement eden kodu yazınız
# ### stack = [a, b, c]
# ### stack.push(d) ---> [a, b, c, d]
# ### stack.pop() ---> [a, b, c]
# ### stack.pop() ---> [a, b]
# ### stack.push(e) ---> [a, b, e]
class Stack:
    
    def __init__(self, items):
        self.Items = items
        
    def push(self, x):
        self.Items.append(x)
        
    def pop(self):
        return self.Items.pop(-1)

stack = Stack(["a", "b", "c"])
print(stack.Items)
stack.push("d")
print(stack.Items)
stack.pop()
print(stack.Items)
stack.pop()
print(stack.Items)
stack.push("e")
print(stack.Items)

