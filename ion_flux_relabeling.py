class Node:
    def __init__(self, root=None):
        self.root = root
        self.left = self.right = None


def solution(h, q):
    nums = list(range(1, 2 ** h))
    height = h
    find = q
    roots = {}
    results = []
    if nums[-1] in q:
        roots[nums[-1]] = -1

    def postorder(height, nums, find):
        if height == 1:
            return Node(nums.pop())
        node = Node()
        node.root = nums.pop()
        node.right = postorder(height-1, nums, find)
        node.left = postorder(height-1, nums, find)
        for number in find:
            if node.left.root == number:
                roots[node.left.root] = node.root
            elif node.right.root == number:
                roots[node.right.root] = node.root
        return node
    postorder(height, nums, find)
    for i in q:
        results.append(roots[i])
    return results
