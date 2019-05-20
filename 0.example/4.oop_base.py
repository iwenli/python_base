# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-20 10:45:07
@LastEditors: iwenli
@LastEditTime: 2019-05-20 11:43:11
@Description: 面向对象编程  && 面向对象高级编程
'''
import types
import enum

__author__ = 'iwenli'


class Student(object):
    count = 0

    def __init__(self, name, score, age=22):
        Student.count += 1
        self.name = name
        self.score = score
        self.__age = age

    def print_score(self):
        print('%s(%s岁):%s分' % (self.name, self.__age, self.score))

    def __str__(self):
        return 'Student object (name=%s)' % self.name

    __repr__ = __str__


class Animal(object):
    def run(self):
        print('Animal is runnig......')


class Dog(Animal):
    def run(self):
        print('Dog is runnig......')


class Cat(Animal):
    def run(self):
        print('Cat is running')


def run_twice(animal):
    animal.run()
    animal.run()


class StudentProp(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score必须是整数")
        elif value < 0 or value > 100:
            raise ValueError("score只能是0-100")
        self._score = value


@enum.unique
class Weekday(enum.Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == '__main__':
    # 类和实例
    # bart = Student('Bart Simpson', 59)
    # lisa = Student('Lisa Simpson', 87, 18)
    # bart.print_score()
    # lisa.print_score()
    # # print(lisa.__age) # 私有属性  禁止访问

    # 继承和多态
    # dog = Dog()
    # cat = Cat()

    # b = Animal()
    # print('dog is Animal:', isinstance(dog, Animal))
    # print('cat is Cat:', isinstance(cat, Cat))
    # c = list()
    # c.append(b)
    # c.append(dog)
    # c.append(cat)
    # for item in c:
    #     item.run()
    # run_twice(Animal())
    # run_twice(Cat())

    # # 获取对象信息
    # print(type(123) == type(234))
    # print(type(123) == int)
    # print(type('123') == str)
    # print(type(Student) == types.FunctionType)
    # print(type(run_twice) == types.FunctionType)
    # print(dir('s'))

    # print(hasattr('as', '__len__'))
    # print(len('as'))

    # # 实例属性和类属性
    # s1 = Student('张三', 67, 16)
    # s2 = Student('李四', 88, 17)
    # s3 = Student('王五', 12, 18)
    # print(Student.count)

    # 使用@property
    # s = StudentProp()
    # s.score = 60  # OK，实际转化为s.set_score(60)
    # print(s.score)  # OK，实际转化为s.get_score()
    # s.score = 9999

    # 定制类
    # print(Student("老虎", 100, 15))

    # 使用枚举类
    Month = enum.Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    print(Month.Jan, Weekday.Fri, Month['Sep'], Weekday(5))
