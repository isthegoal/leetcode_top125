# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
        push(x) -- 将元素 x 推入栈中。
        pop() -- 删除栈顶的元素。
        top() -- 获取栈顶元素。
        getMin() -- 检索栈中的最小元素。

      分析：

      思路：

         一道简单的栈题。

            正常操作比如PUSH, POP, TOP用普通栈A操作，getmin需要借助另一个栈B来记录当前最小值。
            1.新元素PUSH进A时，
              （1） 如果当前B为空栈，就把A也push进B
              （2） 如果当前B不为空，就比较B的栈顶和新元素的大小，把小的那一方PUSH进B
            这样可以保证对于任意时刻的栈A，始终保持栈B的栈顶元素都是栈A元素的最小元素。

            2.当A需要POP元素时，也看看B，需要数字对应 再pop，毕竟B中是最小的，不可以轻易pop,不然不合适。

'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_stack and self.min_stack[-1] <= x:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        num=self.stack[-1]
        self.stack = self.stack[:-1]


        if len(self.min_stack) > 0 and num == self.min_stack[-1]:
            self.min_stack.pop()

        #self.min_stack = self.min_stack[:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

#___________________________________    练习1   ______________________________#
#  非常简单的思路

class MinStack1(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min_stack)==0:
            self.min_stack.append(x)
        else:
            if x<=self.min_stack[-1]:
                self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        num=self.stack[-1]
        self.stack = self.stack[:-1]

        #  对B进行pop时，是本题的核心，需要重点考虑。  （数字得是对应的）
        if len(self.min_stack) > 0 and num == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return 0
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]