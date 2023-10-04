class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = []
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        return "[" + ",".join(result) + "]"


class Solution(object):
    def allPossibleFBT(self, n):
        if n == 1:
            return [TreeNode(0)]

        if n % 2 == 0:
            return []

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
    print(str(tree))
