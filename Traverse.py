class Traverse:

    def preorder(self, root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
