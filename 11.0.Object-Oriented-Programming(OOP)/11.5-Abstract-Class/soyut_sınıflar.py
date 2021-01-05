from abc import ABC, abstractclassmethod

class Animals(ABC):

    @abstractclassmethod
    def run(self): pass

    @abstractclassmethod
    def walk(self): pass 

    def fly(self): 
        print("fly")

class Bird(Animals):
    def __init__(self):
        print("bird")

    def run(self):
        print("run")

    def walk(self):
        print("walk")

kus = Bird()

print(kus.run())
print(kus.walk())
print(kus.fly())

"""
 bir sınıfta tek bir abstractclassmethod olması o sınıfı abstract yapar
 abstract olmayan methodlar da kalıtım yolu ile alt sınıfta kullanılabilir
 """