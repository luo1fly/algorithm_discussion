#!/usr/bin/env python
# Name: 类继承实现单例模式.py
# Time:2016/9/27 9:28
# Author:luo1fly


# import custom modules above

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    m1 = MyClass('caining')
    print(
        'id of m1:%s' % id(m1),
        'name of m1:%s' % m1.name,
        sep='\n'
    )
    m2 = MyClass('shabi')
    print(
        'id of m2:%s' % id(m2),
        'name of m2:%s' % m2.name,
        sep='\n'
    )

