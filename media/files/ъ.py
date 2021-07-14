import abc
# from abc import ABC, abstractclassmethod

# class Abstracklass:
#     def say_hello(self):
#         pass




# class Children(Abstracklass):
#     pass


# children = Children()
# children.say_hello()


class AbctractKlass(abc.ABC):

    @abc.abstractclassmethod
    def say_hello(self):
        print("Call this method in ABC class")

class Hello(AbctractKlass):
    def __init__(self, value):
        self.value = value
    
    def say_hello(self):
        super().say_hello()
        print(self.value)

# abstrac = AbctractKlass()
# abstrac

hello = Hello("Hello world")
hello.say_hello()





