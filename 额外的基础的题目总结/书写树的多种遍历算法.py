# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
    树的深广度优先遍历

    树的先序、中序、后序的  递归 和 非递归方式实现。


'''

#######################################   树的深度遍历 [就是 先序遍历]    ##########################
#第一种形式，使用  递归方式进行实现深度遍历

def DFS(root):
    if root==None:
        return
    print(root.data)
    DFS(root.left)
    DFS(root.right)

#第二种形式  使用栈数据结构进行实现   [当然使用队列  也是可行的]
def DFS_stack(root):
    if root==None:return

    stack=[]
    stack.append(root)

    while(stack):
        new_node=stack.pop()
        #先序遍历，绝对是 先打印，再管左右
        print(new_node.val)

        #使用栈的方式进行这种遍历， 一定要记得  先存右，  再存左，这样 才能让栈先弹出 的  是尽可能往左的先弹出来。   然后每次其实都是按照左边的不断放置，压入
        if new_node.right!=None:
            stack.append(new_node.right)

        if new_node.left!=None:
            stack.append(new_node.left)


#######################################   树的广度遍历 【其实就是层次遍历】    ##########################
#主要  使用队列形式的  遍历方式。
def BFS(root):
    if root==None:
        return

    #定义队列，每次  都按层放到队列中去
    queue=[]
    queue.append(root)

    while queue:
        now_node=queue.pop(0)

        print(now_node.val)

        if now_node.left:
            queue.append(now_node.left)
        if now_node.right:
            queue.append(now_node.right)



#######################################   树的中序遍历 [递归  和  非递归两种形式]    ##########################
#首先是  简单的递归形式
def inorder(root):
    if not root.left and not root.right:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)

# 非递归打印方式      还是使用栈的方法吧    感觉就是  如果还能往左走就一直往左走，  否则 就打印本身，弹出栈并尝试往右走
def inorder2(root):
    stack=[]
    pos=root

    #大环境， 如果栈中有元素，就可以一直往下走
    while pos is not None or  len(stack)>0:
        # 如果指向的不是空结点
        if pos is not None:
            stack.append(pos)
            pos=pos.left
        # 如果指向的是空结点时，那就弹出上一个位置，并进行打印 以及往右看
        else:
            pos=stack.pop()
            print(pos.val)
            pos=pos.right



#######################################   树的后序遍历 [递归  和  非递归两种形式]    ##########################

#首先是  简单的递归形式
def bnorder(root):
    if not root.left and not root.right:
        return

    bnorder(root.left)
    bnorder(root.right)
    print(root.val)

# 书写 麻烦的非递归方式
'''
    使用两个栈进行实现，  
        第一个栈进栈顺序：左节点->右节点->根节点
        第一个栈弹出顺序： 根节点->右节点->左节点(先序遍历栈弹出顺序：根->左->右)
        第二个栈存储为第一个栈的每个弹出依次进栈
        最后第二个栈依次出栈
'''
def post_order(root):
    stack=[root]
    stack2=[]

    while(len(stack)>0):
        node=stack.pop()
        stack2.append(node)

        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    #最终在   stack2中的  结点信息 才是真正最后要 后序打印展示的
    while len(stack2)>0:
        print(stack2.pop().val)

# 感觉上面的有些太麻烦，   现在说下另一种形式的非递归方式，   从逆序的角度进行理解，先按照  根节点->右孩子->左孩子  进行遍历，之后 把序列反过来。
# 经过反过来之后，就是    左孩子->右孩子->根节点  的形式
def post0rder(root):
    #老套路
    if not root:
        return []

    #创建栈  和  用于打印的序列,将来便于 逆序
    stack=[]
    res=[]

    # 栈以及 树不为空的情况下，    使用栈实际就能形成一种 深度遍历的形式
    while stack or root:
        while root:
            stack.append(root)
            res.append(root.val)
            root=root.right
        if stack:
            root=stack.pop()
            root=root.left
    #最后把序列逆序了即可
    return res[::-1]









