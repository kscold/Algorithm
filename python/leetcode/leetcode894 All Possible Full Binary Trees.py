class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n):
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        result = []

        for left_nodes in range(1, n, 2):
            left_subtrees = self.allPossibleFBT(left_nodes)
            right_subtrees = self.allPossibleFBT(n - 1 - left_nodes)

            for left_tree in left_subtrees:
                for right_tree in right_subtrees:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)

        return result

n = int(input())

solution = Solution()
result = solution.allPossibleFBT(n)

for tree in result:
    def treeToList(node):
        if not node:
            return None
        return [node.val, treeToList(node.left), treeToList(node.right)]

    print(treeToList(tree))
