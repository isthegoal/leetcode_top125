# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：实现一个 Trie (前缀树，主要包含字典的含义，是一颗字典树)，包含 insert, search, 和 startsWith 这三个操作。
         这里 insert 是将单词插入到树中，search是进行树中的搜索，找到字符串位置，startsWith


         (前缀树是N叉树的一种特殊形式。通常来说，一个前缀树是用来存储字符串的。前缀树的每一个节点代表一个字符串（前缀）。
         每一个节点会有多个子节点，通往不同子节点的路径上有着不同的字符。子节点代表的字符串是由节点本身的原始字符串，
         以及通往该子节点路径上所有的字符组成的。)

          实现如下示例
            Trie trie = new Trie();
            trie.insert("apple");
            trie.search("apple");   // 返回 true
            trie.search("app");     // 返回 false
            trie.startsWith("app"); // 返回 true
            trie.insert("app");
            trie.search("app");     // 返回 true

          说明:
            你可以假设所有的输入都是由小写字母 a-z 构成的。
            保证所有输入均为非空字符串。

      分析：


      思路：用dict模拟字典树即可。
'''


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        初始定义一个字典
        """
        self.root = {}
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        实现：这个操作和构建链表很像。首先从根结点的子结点开始与 word 第一个字符进行匹配，一直匹配到前缀链上没有对应的字符，
        这时开始不断开辟新的结点，直到插入完 word 的最后一个字符，同时还要将最后一个结点isEnd = true;，表示它是一个单词的末尾。

        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})

        node["end"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        从根结点的子结点开始，一直向下匹配即可，如果出现结点值为空就返回false，如果匹配到了最后一个字符，那我们只需判断node->isEnd即可。
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]

        return "end" in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        前缀匹配：判断 Trie 中是或有以 prefix 为前缀的单词

       实现：和 search 操作类似，只是不需要判断最后一个字符结点的isEnd，因为既然能匹配到最后一个字符，那后面一定有单词是以它
       为前缀的。

        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True

#___________________________________    练习1   ______________________________#
'''
    这里主要是实现那三种操作，通过不断的加深构建，来搭建一个多重的字典：{{a:{r:{e:True}}}，{k}，{d}，{w}}   are
    构建了一种多重的字典来表示前缀树的形式。      核心要记住是搭建了一种多重字典的形式

'''
class Trie(object):
    # 字典树初始定义
    def __init__(self):
        # 初始化创建字典
        self.root={}

    # 往字典树 插入信息,不断的将  每个字符构建到树中
    def __insert__(self,word):
        # 这里不对根部  影响，而是对其下面的孩子 字典产生作用。(所以之后按照根部往下看就行)
        node=self.root
        # 逐步加入字符吧
        for char in word:
            # setdefault() 函数和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值{},就是设置为字典。
            node=node.setdefault(char,{})

        #最后设置个结尾，说明插入完成
        node['end']=True

    def search(self,word):
        # 针对  单词，从上往下进行 字典的 查询即可，直到整个查询结束
        node=self.root

        # 不断的按照字典进行查找
        for char in word:
            if char not in node:
                return False
            # 如果现有路径可行的话，继续往下 进行字典的深查找
            node=node[char]

        # 最后是判别 “end”了，如果能够以  word 结束，那就是完成整个 单词的查询了
        return 'end' in node


    #  接下来 是进行前缀判别，还是比较简单些的。判断 Trie 中是或有以 prefix 为前缀的单词
    def startsWith(self, prefix):
        #和 search 操作相同，只是不需要判断最后一个字符结点的isEnd，因为既然能匹配到最后一个字符，那后面一定有单词是以它为前缀的。
        node=self.root

        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True

