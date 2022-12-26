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

    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        current_node = result

        remains = 0
        while l1 is not None or l2 is not None or remains != 0:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val

            sum = val1 + val2 + remains
            remains = sum // 10

            new_node = ListNode(sum % 10)
            current_node.next = new_node
            current_node = new_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return result.next


list_node1 = ListNode(9)
list_node2 = ListNode(9)

lst1 = [9, 9, 9, 9, 9, 9]
lst2 = [9, 9, 9]

list_node1 = Solution().add_lst(lst1, list_node1)
list_node2 = Solution().add_lst(lst2, list_node2)

x = Solution().addTwoNumbers(list_node1, list_node2)

print(x)
