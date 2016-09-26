#!/usr/bin/env python
# Name: 装饰器实现单例模式.py
# Time:2016/9/26 17:10
# Author:luo1fly


# import custom modules above


def singleton(cls):
    instances = {}
    # 创建一个对象字典维护一个映射关系，以类为key，实例为value

    def wrapper(*args, **kwargs):
        #
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class MyClass(object):
    def __init__(self, n):
        self.n = n
        self.t = []

if __name__ == '__main__':
    c1 = MyClass(1)
    print(
        'id:%s' % id(c1),
        'c1.n:%s' % c1.n,
    )
    c2 = MyClass(2)
    print(
        'id:%s' % id(c2),
        'c2.n:%s' % c2.n,
    )
