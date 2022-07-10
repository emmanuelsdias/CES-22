class Letter ():
    def __init__(self):
        print("start __init__ Letter")
        print("end __init__ Letter")
    

    def what_am_I (self):
        print("I'm a letter!\n")


class Number ():
    def __init__(self):
        print("start __init__ Number")
        print("end __init__ Number")
    

    def what_am_I (self):
        print("I'm a number!\n")


class A (Letter):
    def __init__(self):
        print("start __init__ A")
        super().__init__()
        print("end __init__ A")
    

class One (Number):
    def __init__(self):
        print("start __init__ One")
        super().__init__()
        print("end __init__ One")    
    

class A1 (A, One):
    def __init__(self):
        print("start __init__ A1")
        super().__init__()
        print("end __init__ A1")   
        

class B (Letter):
    def __init__(self):
        print("start __init__ B")
        super().__init__()
        print("end __init__ B")  


class A1B (A1 , B):
    def __init__(self):
        print("start __init__ A1B")
        super().__init__()
        print("end __init__ A1B\n")

    
inheritance = A1B()
inheritance.what_am_I()
print(inheritance.__class__.__mro__)

"""
   Letter
   /   \
  /     \
 / Nmber \
/   |     \
A   1     /
 \  /    /
  A1    B
   \   /
    A1B
"""