import tree.TreeConstructor
from Traverse import Traverse
from tree.TreeConstructor import TreeConst


def main():
    maxnodes = input("\nEnter the Max nodes: ")
    treeconst = TreeConst()
    for i in range(maxnodes):
        printtemp = str(i + 1) + " :"
        temp = input(printtemp)
        treeconst.addnode(treeconst.root, temp)

    while 1:
        print("\nChoose Option -")
        print("1. Insert Element")
        print("2. Delete Element")
        print("3. View Tree1")
        print("4. PreOrder Traverse")
        print("5. PostOrder Traverse")
        print("6. Inorder Traverse")
        print("7. Exit")

        choice = input("Choice - ")

        if choice is 1:
            # insert
            exit(1)
        elif choice is 2:
            # delete
            exit(1)
        elif choice is 3:
            # view
            exit(1)
        elif choice is 4:
            # preorder
            traverse = Traverse()
            traverse.preorder(treeconst.root)
        elif choice is 5:
            # post order
            traverse = Traverse()
            traverse.postorder(treeconst.root)
        elif choice is 6:
            traverse = Traverse()
            traverse.inorder(treeconst.root)
        elif choice is 7:
            # exit
            exit(0
        else:
            print("Incorrect Input. Try again.")


main()
