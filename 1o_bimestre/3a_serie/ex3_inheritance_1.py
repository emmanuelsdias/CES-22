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
    

class OneA (One, A):
    def __init__(self):
        print("start __init__ 1A")
        super().__init__()
        print("end __init__ 1A")   


class OneAB (OneA, B):
    def __init__(self):
        print("start __init__ 1AB")
        super().__init__()
        print("end __init__ 1AB\n")

    
inheritance = OneAB()
inheritance.what_am_I()
print(inheritance.__class__.__mro__)

"""
Number  Letter
  |    /  |
  |   A   |
  |  /    /
 OneA    B
   \    /
   OneAB
"""