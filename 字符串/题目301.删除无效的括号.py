# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：
           删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
            说明: 输入可能包含了除 ( 和 ) 以外的字符。

            示例 1:
            输入: "()())()"
            输出: ["()()()", "(())()"]
            示例 2:

            输入: "(a)())()"
            输出: ["(a)()()", "(a())()"]
            示例 3:

            输入: ")("
            输出: [""]


      分析：


      思路：
    ######### 为何用BFS而不是DFS

        利用BFS理解起来要远远比DFS要简单的多，因为这道题说的是删除最少的括号！！，如果我们每次只删除一个括号，然后观察被删除一个括号后是否合法，如果已经合法了，我们就不用继续删除了啊。因此我们并不需要将遍历进行到底，而是层层深入，一旦达到需求，就不再深入了。

    ######### 如何进行BFS

    我们做BFS，上一层level和下一层level之间的关系为：把所有上一层level中的每个元素都拿出来，列举出在删除一个括号后的所有可能的情况。(不管删除以后是否合法），添加到下一个level中的元素。

    例如：current level是 ["(()", "())"]

    - 那么下一层level中的元素应该是:

        1. 对 "(()" 删除一个括号的所有可能为： (), (), ((
        2. 对 "())" 删除一个括号的所有可能为： (), )), ()
    这六个就是下一个level的全部内容了。

    ######### 如何解决重复的问题

    可是我们发现问题，就是有重复的元素出现。 很简单，我们把level中的list换成set，就避免的重复。

    ######### 如何检查括号是否是个合法括号

    如何检查括号是否是一个合法的括号，这是一个简单题，可以用堆栈，也可以维护计数器。

    ######### 小技巧：

    用filter(func, param) 可以得到param中所有符合条件的元素。 其中判定方法根据func返回的True or False 来决定。

'''
class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(s:str)->bool:
            cnt = 0
            for c in s:
                if c == "(": cnt += 1
                elif c == ")": cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
            return cnt == 0

        # BFS
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid # 如果当前valid是非空的，说明已经有合法的产生了
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":                     # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i]+item[i+1:])
            level = next_level