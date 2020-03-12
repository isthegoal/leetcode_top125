# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个经过编码的字符串，返回它解码后的字符串。
    编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
    你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
    此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

        示例:
        s = "3[a]2[bc]", 返回 "aaabcbc".
        s = "3[a2[c]]", 返回 "accaccacc".
        s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

      分析：本题难点在于括号内嵌套括号，需要从内向外生成与拼接字符串，这与栈的先入后出特性对应。

      思路：

            1.构建辅助栈 stack， 遍历字符串 s 中每个字符 c；
            （1）当 c 为数字时，将数字字符转化为数字 multi，用于后续倍数计算；
            （2）当 c 为字母时，在 res 尾部添加 c；
            （3）当 c 为 [ 时，将当前 multi 和 res 入栈，并分别置空置 00：
                记录此 [ 前的临时结果 res 至栈，用于发现对应 ] 后的拼接操作；
                记录此 [ 前的倍数 multi 至栈，用于发现对应 ] 后，获取 multi × [...] 字符串。
                进入到新 [ 后，res 和 multi 重新记录。
            （4）当 c 为 ] 时，stack 出栈，拼接字符串 res = last_res + cur_multi * res，其中:
                last_res是上个 [ 到当前 [ 的字符串，例如 "3[a2[c]]" 中的 a；
                cur_multi是当前 [ 到 ] 内字符串的重复倍数，例如 "3[a2[c]]" 中的 2。
            2.返回字符串 res。

    这是个大佬的解法，方法还可以：
        时间复杂度 O(N)，递归会更新索引，因此实际上还是一次遍历 s；
        空间复杂度 O(N)，极端情况下递归深度将会达到线性级别。

    动画在这里：https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/

'''
class Solution:
    def decodeString(self, s: str) -> str:

        #stack标识辅助栈，   res记录遇到的字母    multi表示记录乘次数，记录数字
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                #如果是左括号，则将组合信息【次数，有效字串】直接拼接放置到栈中即可
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                # 这里比较难想的地方吧，  得是对应于[内的信息，进行last_res + cur_multi * res的拼接重复，
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            #当遇到 数字时，c的主要作用是设置了 乘的次数，做特殊保存就行。
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/

#___________________________________    练习1   ______________________________#
# 这种解码题， 主要是两点，一点是针对不同符号的应对处理， 另一点是 针对于括号匹配的问题，往往会使用栈的方式，做压入和弹出处理。
# 思考"2[abc]3[cd]ef", 返回 "abcabccdcdcdef"  做推理
def fun1(s):
    # 创建 辅助位置,三个位置分别有不同的作用  stack辅助栈    res记录字母    multi记录数字
    stack,res,multi=[],'',0

    #针对每个字符做处理
    for c in s:
        if c=='[':
            #将左符号部分 其压入栈
            stack.append([multi,res])
            res,multi='',0
        elif c==']':
            #右括号部分 进行字符的拼接  （栈的性质，先进后出）      cur_multi含义是   last_res含义是
            cur_multi,last_res=stack.pop()
            print(cur_multi)
            print(last_res)
            res=last_res+cur_multi*res  #将数字和字母进行拼接
        #遇到数字时，进行记录即可
        elif '0'<=c<='9':
            multi=multi*10 +int(c)
        #遇到字母时，在尾部添加字母即可 （）
        else:
            res+=c
    return res

print(fun1('abcabccdcdcdef'))
