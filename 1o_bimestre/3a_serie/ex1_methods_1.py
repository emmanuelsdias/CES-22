class Nicknames():
    class_nickname = "Nick"

    def __init__(self, instance_nickname):
        self.instance_nickname = instance_nickname


    @staticmethod
    def who_static_knows():
        print("I'm a static method!")
        print("I don't know my class' nickname,")
        print("nor my instance's nickname.\n")
    

    @classmethod
    def who_class_knows(cls):
        print("I'm a class method!")
        print("I know my class' nickname ({}),".format(cls.class_nickname))
        print("but I don't know my instance's nickname.\n")


    def who_instance_knows(self):
        print("I'm an instance method!")
        print("I know my class' nickname ({}),".format(self.class_nickname))
        print("and also my instance's nickname ({}).\n".format(self.instance_nickname))


a = Nicknames("Stan")

# Static method can't access instance's attributes, nor class' attributes
a.who_static_knows()
# Class method can access class'attributes, but can't access instance's attributes
a.who_class_knows()
# Instance method can access both class' and instance's attributes
a.who_instance_knows()


