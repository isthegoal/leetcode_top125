# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：删除无效括号的最小数目，以使输入字符串有效。 返回所有可能的结果。

            “()())()” Output: ["()()()", “(())()”]
            “(a)())()” Output: ["(a)()()", “(a())()”]
            “)(” Output: [""]

      分析：


      思路：这毕竟也是道hard题，解法有好几种。
      【1】BFS暴力求解。把给定字符串排入队中，然后取出检测其是否valid，若合法直接返回；若不合法，对其进行遍历，
      对于是左右括号的字符，去掉括号字符生成一个新的字符串，如果这个字符串之前没有遇到过，将其排入队中。对队列中的每个
      元素都进行相同的检测操作，直到队列为空还没找到valid的字符串的话，就返回空集。
BFS的方法很慢，是level by level的，先去掉所有可能的一个括号，看是否有valid的结果；如果没有，再遍历所有去掉两个括号的可能，再看有无结果…
      【2】经典的DFS递归。
    首先统计多余的半个左或者右括号的数量l和r，要么都为0；要么一个大于0一个等于0；要么两个都大于0（这种情况肯定是有一个右
    括号在最前面）（这样统计的前提是去掉多余的，剩下的确实能左右对应上），isValid函数与上一个解法一致
    递归函数：如果l和r都是0，则说明此时左右括号数目相等，检查是否valid，正确的话加入结果res中；如果l和r还不是0，
    则从start开始遍历，删除多余的半括号，并继续调用递归函数防止重复的结果的方法：对于多个连续的相同的半括号只删除第一个，
    每次要删除时与上一个字符比较，如果相同则直接跳过不考虑，不相同则说明是第一个半括号，防止大量重复计算的方法：每次递归
    开始的位置为start而不是从头开始。
    【3】解法三是较为经典的方式。
    先删除多余右括号，再反转字符串，同样方法删除多余左括号。原理是只要括号相同数量，且没有“)(”的情况则一定valid。比解法二快。

   递归函数的参数中，last_i表示当前遍历到的位置，相当解法二中的start，last_j表示上一个删除的位置，c表明现在需要删除的
   是多余的左括号还是右括号。
   在递归函数中，从last_i开始遍历，在删除右括号的时候，count表示统计到当前位置i时右括号出现的次数，遇到右括号增加1，
   遇到左括号减1。这里遇到右括号为正，即进入第二层for循环进行删除，可以防止字符串开头是)(反向括号的情况，反之删除左括号时亦然。
   count大于0的时候，说明到当前位置i右括号多，即进入第二层for循环开始删除多余右括号：从上一个删除位置last_j开始遍历到当前位置i，
   如果当前是右括号，且是第一个右括号，删除当前右括号，并继续调用递归函数。注意！此第二层for循环结束后要直接返回，必须加return，
   否则会继续进入下面的翻转操作。因为进这个for循环的是右括号多的，不断递归删到最后最多是删成和左括号一样多，不需要再去翻转删左括号。
   count小于等于0时，即当前左括号数量大于等于右括号，直接跳过不进入第二层for循环，继续往右遍历统计“)”，即也不会return；整个字符串
   统计完以后，而是将字符串反转一下，此时反向括号“)(”是valid，继续调用递归函数删除多余的左括号，last_i和last_j均重置为0。
   反转后调用递归函数时需要判断一下c：如果是右括号，说明现在开始要删除左括号；如果是左括号，说明反转已经进行过，那么就可以直接加入结果res了。



'''
#  较为简单的暴力求解法。
class Solution1(object):
    def removeInvalidParentheses(self, s):
        res = []
        curq = set([s]) #初始化时这个set里只有s这一个元素，例如{'(())()('}
        while curq: #当这一层的队列仍然存在时，即上一层没有找到结果，进入下一层
            nxtq = set() #去掉一个括号的所有可能字符串存入其中，相当于BFS的下一层

            #遍历这一层的队列中的所有字符串
            while curq:
                p = curq.pop() #pop出来的是一整个s
                if self.isValid(p):
                    res.append(p)
                if not res: #本层只要找到一个结果res，就不会进入下一层，即不会多删一个括号来找
                    for i in range(len(p)):
                        if p[i] in '()': #防止是字母
                            nxtq.add(p[:i] + p[i+1:])

            if res: #这一层找到了结果
                return res
            else:
                curq = nxtq #进入下一层
        return res #万一没有找到任何结果

    def isValid(self, s):
    #从左向右遍历valid字符串，左括号的数量只可能小于等于右括号的数量，字符串结束时，必两者相等
        left = 0
        for c in s:
            if c == '(': left += 1
            elif c == ')': left -= 1
            if left < 0: return False
        return left == 0


# 第二种，DFS递归的方式。
class Solution2:
    def removeInvalidParentheses(self, s: str):
        l, r = 0, 0
        self.res = []
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        self.DFS(s, 0, l, r)
        return self.res

    def isValid(self, s):
        left = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                left -= 1
            if left < 0: return False
        return left == 0

    def DFS(self, s, start, l, r):
        if l == 0 and r == 0:
            if self.isValid(s):
                self.res.append(s)
            return
            # 这里不加return也可以通过，因为l和r都等于0时，
        for i in range(start, len(s)):
            if i != start and s[i] == s[i - 1]: continue
            if r > 0 and s[i] == ')': self.DFS(s[:i] + s[i + 1:], i, l, r - 1)
            if l > 0 and s[i] == '(': self.DFS(s[:i] + s[i + 1:], i, l - 1, r)



# 第三种，对括号进行直接处理的方式。  使用DFS的方式进行多余括号的删除。
class Solution:
    def removeInvalidParentheses(self, s):
        self.res = []
        self.DFS(s, ')', 0, 0)
        return self.res

    def DFS(self, s, c, last_i, last_j):
        count = 0
        for i in range(last_i, len(s)):
            if s[i] == '(' or s[i] == ')':
                if s[i] == c:
                    count += 1
                else:
                    count -= 1
            if count <= 0: continue
            for j in range(last_j, i + 1):
                if s[j] == c and (j == last_j or s[j] != s[j - 1]):
                    self.DFS(s[:j] + s[j + 1:], c, i, j)
            return  # break out of DFS function directly
        s = list(s)[::-1]
        s = ''.join(s)
        if c == ')':
            self.DFS(s, '(', 0, 0)
        else:
            self.res.append(s)
