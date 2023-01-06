# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        end = ListNode(val)
        n = self
        while n.next:
            n = n.next
        n.next = end


class Solution:
    def add_lst(self, lst, list_node):
        for i in range(len(lst)):
            list_node.append(lst[i])
        return list_node

    def middleNode(self, head):
        c, p = 1, head

        while p.next:
            c += 1
            p = p.next

        i, p = 1, head

        while i != c // 2 + 1:
            p = p.next
            i += 1

        return p


list_node1 = ListNode(1)

lst1 = [2, 3, 4, 5, 6]

list_node1 = Solution().add_lst(lst1, list_node1)

solution = Solution().middleNode(list_node1)

