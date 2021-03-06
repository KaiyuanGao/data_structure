#!/usr/bin/python
#coding=utf-8


#二叉树的list实现

def BinTree(data, left = None, right= None):				#构造函数
	return [data, left, right]

def is_empty(btree):
	return btree is None
	
def root(btree):
	return btree[0]
	
def left(btree):
	return btree[1]
	
def left(btree):
	return btree[2]
	
def set_root(btree,data):
	btree[0]= data
	
def set_left(btree,left):
	btree[1]= left
	
def set_right(btree,right):
	btree[2]= right




###二叉树的链接实现

class Node(object):     #结点类
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):		#二叉树类
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):		#为树添加节点
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。


    def front_digui(self, root):		#利用递归实现树的先序遍历
        if root == None:
            return
        print (root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)


    def middle_digui(self, root):		#利用递归实现树的中序遍历
        if root == None:
            return
        self.middle_digui(root.lchild)
        print (root.elem)
        self.middle_digui(root.rchild)


    def later_digui(self, root):         #利用递归实现树的后序遍历
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print (root.elem)


    def front_stack(self, root):          #利用堆栈实现树的先序遍历
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                print(node.elem)
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rchild                  #开始查看它的右子树


    def middle_stack(self, root):			#利用堆栈实现树的中序遍历
        if root == None:
            return
        myStack = []						#创建空堆栈
        node = root							#从根结点出发
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.elem)
            node = node.rchild                  #开始查看它的右子树


    def later_stack(self, root):             #利用堆栈实现树的后序遍历
        if root == None:
            return
        myStack1 = []
        myStack2 = []					#后序遍历需要将结点二次入栈
        node = root
        myStack1.append(node)
        while myStack1:                   #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:                         #将myStack2中的元素出栈，即为后序遍历次序
            print (myStack2.pop().elem)


    def level_queue(self, root):				#利用队列实现树的层次遍历
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)			#将根结点指针入队
        while myQueue:					#队列非空则执行
            node = myQueue.pop(0)	
            print(node.elem)			#访问从队列中取出的元素
            if node.lchild != None:		#若元素所指结点的左右孩子结点非空，则将其左右孩子的指针顺序入队
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)



    











			
