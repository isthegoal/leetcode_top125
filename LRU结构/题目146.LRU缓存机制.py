# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

      获取数据 get(key) -         如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
      写入数据 put(key, value) -  如果密钥不存在，则写入其数据值。当缓存容量达到上限时，
                                  它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

      并尽量在O(1) 时间复杂度内完成读取和插入 这两种操作

      分析：
      思路：要O（1）的操作复杂度，基本就是用哈希表。

            这里其实可以看出 核心是要 实现写入操作，重要的意义是删除掉最近最少使用的数据值， 怎么实现呢，方法就是get操作本身就是一种使用的含义。

            因此在使用时将数据放到最前面，这样在put时，也是同样的，把最新的数据放置到末尾中，表示最优先 put操作时排出的。

'''

'''
  OrderedDict 也是 dict 的子类，其最大特征是，它可以“维护”添加 key-value 对的顺序。简单来说，就是先添加的 key-value 对排在前面，
后添加的 key-value 对排在后面。

  popitem() 方法 ：返回并删除字典中的最后一对键和值

'''
from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type record: OrderedDict     表示自带的一种有前后加入顺序的字典
        :type capacity: int           表示字典容器中剩余的空间数量

        """
        self.record = OrderedDict()
        self.capacity = capacity

    #实现LRU的取除key对应数的功能
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print self.record     如果key在这个特殊字典中，直接进行弹出即可，同时刷新下其位置，让其位于最靠前的位置（按照最新最少原则，最优先剔除）。
        if key in self.record:  # 已经存在
            tmp = self.record.pop(key)
            self.record[key] = tmp  # 利用OrderedDict的性质，刷新它为最新key
            return self.record[key]
        else:
            return -1



    #先LRU实现按照 key:value 方式存放到字典Dict中去
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        #第一步是腾位置的过程，我们首先看是否存在，如果存在的话，就先拿出来，等在放在最后的位置。
        if key in self.record:  # 当前key有旧的值
            self.record.pop(key)
        else:
            #如果之前未存在时，就要考虑是否有剩余空间的问题，如果没有的话，就把最老的数清理出去。
            if self.capacity > 0:  # 还有空位
                self.capacity -= 1
            else:  # 没有空位，就把最老的拿出来 （python中自带的这种容器操作还是要熟悉下吧，popitem）
                self.record.popitem(last=False)

        #重要的是把当前要放入的，放到最后，也就是 放在LRU最优先的地方。
        self.record[key] = value



###############################    练习区1   #############################
    #主要的 put操作的复写
    def put1(self,key,value):
        if key in self.record:
            self.record.pop(key)
        else:
            if self.capacity>0:
                self.capacity-=1
            else:
                self.record.popitem(last=False)
        self.record[key]=value