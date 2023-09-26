class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
             list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


values1 = input().split()
list1 = None
for val in reversed(values1):
    list1 = ListNode(int(val), list1)

values2 = input().split()
list2 = None
for val in reversed(values2):
    list2 = ListNode(int(val), list2)

solution = Solution()

merged_list = solution.mergeTwoLists(list1, list2)

while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
