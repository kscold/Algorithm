import sys


input = sys.stdin.readline
class Node():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


def rangeSumBST(self, root, low, high):
    self.sum = 0 # self에 sum을 합
    self.low = low
    self.high = high

    def dfs(node):
        if not node: # 노드가 없으면 리턴
            return

        dfs(node.right) # 노드의 오른쪽을

        if node.val >= self.low and node.val <= self.high: #
            self.sum += node.val

        elif node.val < self.low:
            return

        dfs(node.left)

    dfs(root)

    return self.sum





bst_input = list(map(int, input))
bst = rangeSumBST()



