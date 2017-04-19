# -*- coding: utf-8 -*-
class BinaryTreeNode:
    def __init__(self,data,left,right):
        self.left=left
        self.data=data
        self.right=right
class BinaryTree:
    def __init__(self):
        self.root=None
    def makeTree(self,data,left,right):
        self.root = BinaryTreeNode(data,left,right)

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False
    def perOrder(self,r):
        if r.root is not None:
            print r.root.data
            if r.root.left is not None:
                self.perOrder(r.root.left)
            if r.root.right is not None:
                self.perOrder(r.root.right)
    def postOrder(self,r):
        if r.root is not None:
            if r.root.left is not None:
                self.postOrder(r.root.left)
            if r.root.right is not None:
                self.postOrder(r.root.right)
            print r.root.data

    def inOrder(self,r):
        if r.root is not None:
            if r.root.left is not None:
                self.inOrder(r.root.left)
            print r.root.data
            if r.root.right is not None:
                self.inOrder(r.root.right)

r=BinaryTree()
ra=BinaryTree()
ra.makeTree(2,None,None)
rb=BinaryTree()
rb.makeTree(3,None,None)
r.makeTree(1,ra,rb)

#先序排列
r.perOrder(r)
#后序排列
r.postOrder(r)
#中序排列
r.inOrder(r)