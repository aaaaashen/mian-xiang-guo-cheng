class Person:
    """
定义类
    """
    def eat(self):
        """
        实例方法（带self）
        :return:
        """
        print(self)
        pass
    pass
#self只有在类中定义 实例方法的时候才有意义 ，在调用时直接 （）即可，不用传入相应参数，而是自动指向


xiaoming=Person()
"""
实例对象
"""
xiaoming.eat()
print(xiaoming.eat)
print(id(xiaoming.eat))#都是一个东西