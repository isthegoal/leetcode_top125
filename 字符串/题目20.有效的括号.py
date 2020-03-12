# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
            有效字符串需满足：
                左括号必须用相同类型的右括号闭合。
                左括号必须以正确的顺序闭合。
                注意空字符串可被认为是有效字符串

          示例 1:
              输入: "()"
              输出: true
          示例 2:
              输入: "()[]{}"
              输出: true

      分析：一道leetcode简单题，直接使用栈的思想就可以搞定了


      思路：处理右括号需要看前面有没有匹配的左括号，所以可以用栈。每次左括号就压进栈，右括号就看栈顶是不是匹配的左括号，如果不是说明有问题，
      比如 [ )，就无法匹配上，如果匹配上了，就把栈顶pop掉。最后判断是不是栈里所有左括号都脱单了。
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {")": "(", "]": "[", "}": "{"}
        stack = []

        #对于  s中的每个字符，一个个进行栈角度上的判别
        for i, char in enumerate(s):
            #如果  字符之前未出现过，那就直接压入栈吧
            if char not in mapping:  # left
                stack.append(char)
            else:
                #重要的合法性判别，如果  栈不为空，同时  栈最上面的并不是我们所要   匹配的，那就说说明不合法。
                if not stack or stack[-1] != mapping[char]:
                    return False

                #合法情况下的直接 弹出操作。
                stack.pop()

        return len(stack) == 0

#___________________________________    练习1   ______________________________#
#直接使用栈     进行符号组合上的合法性判断即可
def fun1(s):
    mapping={')':'(',']':'[','}':'{'}
    stack=[]
    # 对于s字符上的每个字符，不断进行栈拼接 角度上的判别
    for i,char in enumerate(s):
        # 如果 是位于左包含的符号，直接压入栈中
        if char not in mapping:
            stack.append(char)
        else:
            #如果是 位于右包含的字符  ,那就进行非法性的判断，（下面两个是产生非法的条件）
            if not stack or stack[-1] !=mapping[char]:
                return False

            #如果是合法时，进行弹出
            stack.pop()

    return len(stack)==0