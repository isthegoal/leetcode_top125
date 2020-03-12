
'''
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是?push to back, peek/pop from front, size, 和?is empty?这些操作是合法的。
你所使用的语言也许不支持队列。?你可以使用 list 或者 deque（双端队列）来模拟一个队列?, 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

'''

from collections import deque
'''
根据题意，只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
'''


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 这里设定用两个  队列 来模拟栈   。  一个用来 进， 一个用来出
        # 因为使用队列，所以只能使用队列的 append  和 popleft操作[0]，先进先出，通过两个操作实现 栈。
        self.queue1 = deque()  # in
        self.queue2 = deque()  # out

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        #  压栈操作时，直接放入即可
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        三步实现  pop弹出栈操作
        """
        #  首先进行为空判别
        assert not self.empty(), 'Empty stack!'

        # 第一步  ，不断将que1的元素放置到  que2中去，但是留下一个
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # 第二步，因为 我们是需要 最后一个放到队列的， 所以que1 中最后一个剩下的 就是符合意思的。
        ret = self.queue1.popleft()
        # 第三步，进行队列意义上的归位，让queue1 始终作为进的含义
        self.queue1, self.queue2 = self.queue2, self.queue1

        # 最后获取 弹出值，搞定
        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int

        获取栈顶元素

        获取堆顶，好就像 pop时候的操作一样，找到最后进的那个
        """
        #  获取顶部的信息，但是这里因为是队列，所以必须使用队列专门的操作
        assert not self.empty(), 'Empty stack!'

        # 进行  倒 队列
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        #  从queue1的最后一个，表示最后一个放入队列的元素，也就是栈需要弹出的。  （这样其实已经获得了 目标）
        ret = self.queue1[0]

        # 最后的一些还原操作，  首先把获取到的top也得放到que2中，这样再完整的 变成变量queue1.
        self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

        return ret

    def empty(self):
        """
        Returns whether the stack is empty.     全空时为空
        :rtype: bool
        """
        #  两个同时 没了，就空了
        return len(self.queue1) == 0 and len(self.queue2) == 0


#___________________________________    练习1   ______________________________#
# 使用  两个队列 来实现一个栈，这里主要还是限制了  只能使用队列中的queue[0]  获取最先进的和  append操作。   比较麻烦的还是模仿的pop和top操作
class MyStack1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 这里设定用两个  队列 来模拟栈   。  一个用来 进， 一个用来出
        # 因为使用队列，所以只能使用队列的 append  和 popleft操作[0]，先进先出，通过两个操作实现 栈。
        self.queue1 = deque()  # in
        self.queue2 = deque()  # out

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        #  压栈操作时，直接放入即可
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        三步实现  pop弹出栈操作
        """
        #  首先进行为空判别
        assert not self.empty(), 'Empty stack!'

        # 第一步  ，不断将que1的元素放置到  que2中去，但是留下一个
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # 第二步，因为 我们是需要 最后一个放到队列的， 所以que1 中最后一个剩下的 就是符合意思的。
        ret = self.queue1.popleft()
        # 第三步，进行队列意义上的归位，让queue1 始终作为进的含义
        self.queue1, self.queue2 = self.queue2, self.queue1

        # 最后获取 弹出值，搞定
        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int

        获取栈顶元素

        获取堆顶，好就像 pop时候的操作一样，找到最后进的那个。

        这里相对pop操作要多了一步，四小步即可.....
        """
        #  获取顶部的信息，但是这里因为是队列，所以必须使用队列专门的操作
        assert not self.empty(), 'Empty stack!'

        # 1.进行  倒 队列
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        #  2.从queue1的最后一个，表示最后一个放入队列的元素，也就是栈需要弹出的。  （这样其实已经获得了 目标）
        ret = self.queue1[0]

        # 3.最后的一些还原操作，  首先把获取到的top也得放到que2中，这样再完整的 变成变量queue1.
        self.queue2.append(self.queue1.popleft())
        # 4.还原含义
        self.queue1, self.queue2 = self.queue2, self.queue1

        return ret

    def empty(self):
        """
        Returns whether the stack is empty.     全空时为空
        :rtype: bool
        """
        #  两个同时 没了，就空了
        return len(self.queue1) == 0 and len(self.queue2) == 0

