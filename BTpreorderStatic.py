class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

    def AddNode(self,node,data):
        if node is None:
            self.root=TreeNode(data)
        else:
            if data<node.data:
                if node.left is None:
                    node.left=TreeNode(data)
                else:
                    self.AddNode(node.left,data)
            else:
                if node.right is None:
                    node.right=TreeNode(data)
                else:
                    self.AddNode(node.right,data)
        print("Added...")


    def preorder(self,root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)


def main():
    print("halt")
    tree = Tree()
    tree.AddNode(tree.root,40)
    tree.AddNode(tree.root,20)
    tree.AddNode(tree.root,60)
    tree.AddNode(tree.root,10)

    tree.preorder(tree.root)
    
    print("program executed successfully");


main()

