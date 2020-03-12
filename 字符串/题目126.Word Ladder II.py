# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
            每次转换只能改变一个字母。转换过程中的中间单词必须是字典中的单词。
            说明:如果不存在这样的转换序列，返回一个空列表。所有单词具有相同的长度。所有单词只由小写字母组成。字典中不存在重复的单词。
            你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

            示例 1:
                输入:
                beginWord = “hit”,
                endWord = “cog”,
                wordList = [“hot”,“dot”,“dog”,“lot”,“log”,“cog”]
                输出:
                [
                [“hit”,“hot”,“dot”,“dog”,“cog”],
                [“hit”,“hot”,“lot”,“log”,“cog”]
                ]

            示例 2:
                输入:
                beginWord = “hit”
                endWord = “cog”
                wordList = [“hot”,“dot”,“dog”,“lot”,“log”]
                输出: []

      分析：
             这道题有点high，一道hard题，

      思路：
                思路与127题相同，因为要统计所有可能，所以可以利用字典q储存单词转换过程，记录该单词可以由那些单词转换成，特殊情况q[beginWord ]=[beginWord ],	q[endWord ]=[endWord ]
                例如示例1
                q[‘hit’]= [‘hit’],
                q[‘hot’]=[‘hit’],
                q[‘dot’]=[‘hot’],
                q’[lot’]= [‘hot’],
                q[‘cog’]= [‘cog’],
                q[‘dog’]= [‘cog’, ‘dot’],
                q[‘log’]=[‘lot’, ‘cog’]
                按照127题思路，两头同时算 ,当相遇时，统计相遇的单词
                在示例1中 统计结果为{‘log’, ‘dog’}
                将去q[t]中的一个元素作为key循环下去，最后一定会到达beginWord 或endWord

      https://blog.csdn.net/qq_37369124/article/details/88147596

'''


def findLadders(self, beginWord, endWord, wordList):
    q = {beginWord: {beginWord}}
    z = set()  # 统计相遇节点
    wl = len(beginWord)
    begin_set, end_set = {beginWord}, {endWord}
    wordList = set(wordList)
    if endWord not in wordList: return []
    i = 1
    while begin_set and end_set:
        i = i + 1
        if len(begin_set) > len(end_set): begin_set, end_set = end_set, begin_set
        nextList = set()
        u = 0
        for word in begin_set:
            for j in range(wl):
                for k in range(26):
                    nextWord = word[:j] + chr(k + 97) + word[j + 1:]
                    if nextWord in end_set:
                        z.add(nextWord)
                        if (nextWord in q):
                            q[nextWord].add(word)
                        else:
                            q[nextWord] = {word}
                    elif nextWord in wordList:
                        if (nextWord in q):
                            q[nextWord].add(word)
                        else:
                            q[nextWord] = {word}
                        if (nextWord not in nextList): nextList.add(nextWord)
        for www in nextList: wordList.remove(www)
        if z != set():  return self.g(beginWord, endWord, z, q)  # 因为要求的是最短路径，有结果直接返回就是了
        begin_set = nextList
    return []


def g(self, beginWord, endWord, z, q):
    for i in q:
        q[i] = list(q[i])
    e = []
    for w in z:
        l = self.f(q, w)  # 将结果相连成小段
        l1 = []
        l2 = []
        for i in l:
            if (i[-1] == beginWord):
                l1.append(i)
            elif (i[-1] == endWord):
                l2.append(i)
            if (i[0] == endWord and i[-1] == beginWord):
                e.append(i[::-1])  # 长度为2
            elif (i[0] == beginWord and i[-1] == endWord):
                e.append(i)
        for a in l1:
            for b in l2: e.append(a[::-1] + b[1:])  # 前后小段相连成完整段
    return e


def f(self, q, word):
    if (q[word][0] == word): return [[word]]  # 到了beginWord 或是 endWord
    e = []
    for i in q[word]:
        for w in self.f(q, i):
            e.append([word] + w)
    return e










#第二种思路：
     # 这是一个最短路径问题。首先将beginWord放进队列，当队列不为空的时候，pop出第一个数，将它周围的在字典的push进队列。
     # 要注意的是将字段的数push进队列的同时，将其路径用dict记录下来。
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        ans,q = {},[]
        q.append(beginWord)
        ans[beginWord] = [[beginWord]]
        ans[endWord] = []
        while len(q) != 0:
            tmp = q.pop(0)
            for i in range(len(beginWord)):
                part1,part2 = tmp[:i],tmp[i + 1:]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if tmp[i] != j:
                        newword = part1 + j + part2
                        if newword == endWord:
                            for k in ans[tmp]:
                                ans[endWord].append(k + [endWord])
                            while len(q) != 0:
                                tmp1 = q.pop(0)
                                if len(ans[tmp1][0]) >= len(ans[endWord][0]):
                                    break
                                for ni in range(len(beginWord)):
                                    npart1,npart2 = tmp1[:ni],tmp1[ni+1:]
                                    for nj in "abcdefghijklmnopqrstuvwxyz":
                                        if tmp1[ni] != nj:
                                            nw = npart1 + nj + npart2
                                            if endWord == nw:
                                                for nk in ans[tmp1]:
                                                    ans[endWord].append(nk + [endWord])
                            break
                        if newword in wordlist:
                            q.append(newword)
                            ans[newword] = []
                            for k in ans[tmp]:
                                ans[newword].append(k + [newword])
                            wordlist.remove(newword)
                        elif newword in ans and len(ans[newword][0]) == len(ans[tmp][0]) + 1:
                            for k in ans[tmp]:
                                ans[newword].append(k + [newword])
        return ans[endWord]