# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：

          请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
          若队列为空，pop_front 和 max_value 需要返回 -1

            示例 1：

            输入:
            ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
            [[],[1],[2],[],[],[]]
            输出: [null,null,null,2,1,2]
            示例 2：

            输入:
            ["MaxQueue","pop_front","max_value"]
            [[],[],[]]
            输出: [null,-1,-1]


      分析：  这里感觉 就是定义一个队列，但是有两个点需要注意：
                【1】 需要 实现一个获取 队列最大值的函数  max_value
                【2】 对时间复杂度上有限制，需要 限定 三种操作 平均的时间复杂度在 O(1)

      思路：

'''

class MaxQueue(object):

    def __init__(self):
        self.queue=[]

    def max_value(self):
        """
        :rtype: int
        """
        #  最大值的获取，使用python真的很简单，直接 max就能得到了。
        if self.queue:
            return max(self.queue)
        else:
            return -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)


    def pop_front(self):
        """
        :rtype: int
        """
        # 队列为空的情况
        if not self.queue:
            return -1
        else:
            # 队列不为空时，弹出 第一个加入的 并 删除掉
            s= self.queue[0]
            del self.queue[0]
            return s