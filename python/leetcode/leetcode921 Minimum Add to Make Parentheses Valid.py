# class Solution(object):
#     def minAddToMakeValid(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         stack = []
#         for c in s:  # 문자열을 순회
#             if not stack:  # 스텍에 아무것도 없으면
#                 stack.append(c)  # 문자를 추가
#                 continue  # 그 다음 문자 순회
#             if stack[-1] == '(' and c == ')':  # 스택의 가장 마지막 문자가 ( 고 현재 순회 중인 문자가 )면
#                 stack.pop()  # ( 문자를 스택에서 pop
#             else:  # 스택이 비어있지 않고 )라면 또는 스택에 (가 차있고 또 (가 들어온다면
#                 stack.append(c)  # ) 문자를 추가
#
#         return len(stack)


class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        add = 0
        ex = 0
        for c in s:
            if c == "(":
                add += 1
            elif c == ")" and add <= 0:
                ex += 1
                add = 0
            else:
                add -= 1
        return add + ex


solution = Solution()
result = solution.minAddToMakeValid("())(()")
print(result)
