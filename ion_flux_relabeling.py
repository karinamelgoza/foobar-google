class Node:
    def __init__(self, root=None):
        self.root = root
        self.left = self.right = None

    def PrintTree(self):
        print(self.root)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()

    def findval(self, lkpval):
        if lkpval < self.root:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.root:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.root) + ' is found')


def postorder(height, nums):
    if height == 1:
        return Node(nums.pop())
    node = Node()
    node.root = nums.pop()
    node.right = postorder(height-1, nums)
    node.left = postorder(height-1, nums)
    return node


height = 5
tree = postorder(height, list(range(1, 2 ** height)))
# tree.PrintTree()
print(tree.findval(21))
