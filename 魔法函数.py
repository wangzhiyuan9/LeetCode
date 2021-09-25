class test(object):
    def __init__(self,*args):
        self.a = args[0]
        self.b = args[1]
        self.change={'python':'This is python',
                     'php':'PHP is a good language'}
        self.names = args
    """
        输出实例化对象显示  str优先级高于repr
    """
    # 面向用户的显示 
    def __str__(self) -> str:
        return "test(%d,%d)"%(self.a,self.b)
    # 面向交互及用户的显示
    def __repr__(self) -> str:
        return "test(%d,%d)"%(self.a,self.b)

    """
        属性相关
    """
    # 访问一个不存在的属性的时候，提示不存在这个属性
    def __getattr__(self,item)->str:
        return "can not find attr %s"%item

    
    """
        集合、序列相关
    """
    # 获取某个对象长度
    def __len__(self)->int:
        return len(self.names)

    # 让对象实现迭代功能
    def __getitem__(self,key):
        # return self.change[index]

        # 获取初始化变量的值  key为a,b,names时返回对应的值,否则返回default
        # return self.__dict__.get(key, "default")

        # 初始化字典d中的值
        return self.change[key]

    # 按一定的方式存储和key相关的value。在设置类实例属性时自动调用的
    def __setitem__(self,key,value):
        self.change[key] = value
    
    # 在对对象的组成部分使用__del__语句的时候被调用，删除与key相关联的值。同样，仅当对象可变的时候，才需要实现这个方法。
    def __delitem__(self, key):
        del self.change[key]

    # 判断一个定点是否包含在里面
    def __contains__(self,x) -> bool: 
        return x in self.change


    """
        迭代相关
    """
    # 使用__iter__方法令对象可迭代
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.a < self.b:
            ret = self.a
            self.a += 1
            return ret
        else:
            raise StopIteration
t = test(1,2,"a")
print("__str__")
print(t)
print("__len__")
print(len(t))
print("__getitem__")
print(t['php'])
t['test'] = "succuss"
print(t.test)
print(t['test'])
del t['test']
print(t.change)
print("A" in t)
print("python" in t)

for item in test(1,4,"a"):
    print(item)




# 每次产生的数据，是产生一个用一个，
# 比如要遍历[0, 1, 2, 3.....]一直到10亿，
# 如果使用列表的方式，那么是会全部载入内存的，
# 但是如果使用迭代器，可以看见，当用到了(也就是在调用了next)才会产生对应的数字，
# 这样就可以节约内存了，这是一种懒惰的加载方式。
a = test(1,5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a))
print('Test')




