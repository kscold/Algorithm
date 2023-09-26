class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head

        reversedhead = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return reversedhead

def createreverseList(values):
    head = None
    for val in reversed(values):
        new_node = ListNode(int(val))
        new_node.next = head
        head = new_node
    return head

values = input().split()
head = createreverseList(values)

solution = Solution()

reversed_head = solution.reverseList(head)

while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next
