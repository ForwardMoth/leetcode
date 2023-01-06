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

    def removeNthFromEnd(self, head, n):
        c, p = 1, head

        while p.next:
            c += 1
            p = p.next

        p = head
        for i in range(c - n - 1):
            p = p.next

        """if need to del not head element"""
        if c != n:
            prev_del = p
            cur_del = p.next if p.next else None
            next_del = p.next.next if cur_del and cur_del.next else None
            """if list had 1 element"""
            if cur_del is None:
                return None
            else:
                prev_del.next = next_del
                del cur_del

            return head
        else:
            head = head.next
            del p

            return head


list_node1 = ListNode(1)

lst1 = [2]

n = 2

list_node1 = Solution().add_lst(lst1, list_node1)

solution = Solution().removeNthFromEnd(list_node1, n)
