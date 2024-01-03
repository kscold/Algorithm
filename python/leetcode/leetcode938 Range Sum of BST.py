class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right)
            if node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root) # root를 매개변수 node에 넣음


# 주어진 리스트로부터 이진 트리 생성
def createTree(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = [root]
    i = 1

    while queue and i < len(nums):
        node = queue.pop(0)

        left_val = nums[i]
        i += 1
        right_val = nums[i]
        i += 1

        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)

        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)

    return root


# 주어진 입력 리스트
# input_list = [10,5,15,3,7,None,18]

# 주어진 입력 문자열
input_str = input().split()

# "null"을 None으로 변환하고 숫자로 변환
input_list = [int(x) if x != "null" else None for x in input_str]

# 이진 트리 생성
tree_root = createTree(input_list)

# Solution 클래스의 인스턴스 생성
solution = Solution()

# rangeSumBST 메서드 호출
low, high = map(int, input().split())

result = solution.rangeSumBST(tree_root, low, high)
print(result)  # 결과 출력
