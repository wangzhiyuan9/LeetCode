"""
    动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，
    或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，
    比如enqueue、dequeueAny、dequeueDog和dequeueCat。允许使用Java内置的LinkedList数据结构。
    enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。
    dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。

    示例1:
        输入：
            ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
            [[], [[0, 0]], [[1, 0]], [], [], []]
        输出：
            [null,null,null,[0,0],[-1,-1],[1,0]]

    示例2:
        输入：
            ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]
            [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
        输出：
            [null,null,null,null,[2,1],[0,0],[1,0]]
"""
from typing import List
class AnimalShelf:
    def __init__(self):
        self.dog = []
        self.cat = []
    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.cat.insert(0,animal[0])
        else:
            self.dog.insert(0,animal[0])
    def dequeueAny(self) -> List[int]:
        if not self.dog and not self.cat:
            return [-1,-1]
        elif self.dog and not self.cat:
            return self.dequeueDog()
        elif not self.dog and self.cat:
            return self.dequeueCat()
        else:
            if self.cat[-1] < self.dog[-1]:
                return self.dequeueCat()
            else:
                return self.dequeueDog()
    def dequeueDog(self) -> List[int]:
        if self.dog:
            return [self.dog.pop(),1]
        return [-1,-1]
    def dequeueCat(self) -> List[int]:
        if self.cat:
            return [self.cat.pop(),0]
        return [-1,-1]




obj = AnimalShelf()
obj.enqueue([0,0])
obj.enqueue([1,0])
param_1 = obj.dequeueCat()
param_2 = obj.dequeueDog()
param_3 = obj.dequeueAny()
print(param_1,param_2,param_3)