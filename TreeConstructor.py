from TreeNode import TreeNode


class TreeConst:
    def __init__(self):
        self.root = None

    def addnode(self, node, data):
        if node is None:
            self.root = TreeNode(data)
        else:
            if data < node.data:
                if node.left is None:
                    node.left = TreeNode(data)
                else:
                    self.addnode(node.left, data)
            else:
                if node.right is None:
                    node.right = TreeNode(data)
                else:
                    self.addnode(node.right, data)








