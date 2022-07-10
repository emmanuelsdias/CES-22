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
    

class B (Letter):
    def __init__(self):
        print("start __init__ B")
        super().__init__()
        print("end __init__ B")  


class One (Number):
    def __init__(self):
        print("start __init__ One")
        super().__init__()
        print("end __init__ One")    
    

class B1 (B, One):
    def __init__(self):
        print("start __init__ B1")
        super().__init__()
        print("end __init__ B1")   


class AB1 (A, B1):
    def __init__(self):
        print("start __init__ AB1")
        super().__init__()
        print("end __init__ AB1\n")

    
inheritance = AB1()
inheritance.what_am_I()
print(inheritance.__class__.__mro__)

"""
Letter  Number
  | |    |
  | B    1
  |  \  /
  A   B1
   \ /
   AB1
"""