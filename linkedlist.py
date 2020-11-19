class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        if self.head is None:
            print("LL is empty")
            return
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("no previous node")
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def delete_node(self, key):
        cur = self.head
        if cur is not None and cur.data == key:
            self.head = cur.next
            cur = None
            return llist

        prev = None
        while cur and cur.data !=key:
            prev = cur
            cur = cur.next

        if cur is None:
            print("not found")
            return

        prev.next = cur.next
        cur = None

    def swap_node(self, key1, key2):
        if key1 == key2:
            return

        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data != key1:
            prev_1 = cur_1
            cur_1 = cur_1.next

            prev_2 = None
            cur_2 = self.head
            while cur_2 and cur_2.data != key2:
                prev_2 = cur_2
                cur_2 = cur_2.next

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def rev_list(self):
        cur = self.head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        self.head = prev
        return

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        if not p is not None :
            return q

        if not q is not None:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next

            else:
                s.next = q
                s = q
                q = s.next
        if not p is not None:
            s.next = q
        if not q is not None:
            s.next = p
        return new_head

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        sum_llist = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data

            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            # print(s)
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.insert_at_end(remainder)
            else:
                carry = 0
                sum_llist.insert_at_first(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_llist.print_list()


llist_1 = LinkedList()
llist_2 = LinkedList()
llist_1.insert_at_end(5)
llist_1.insert_at_end(6)
llist_1.insert_at_end(3)

llist_2.insert_at_end(8)
llist_2.insert_at_end(4)
llist_2.insert_at_end(2)

# llist = LinkedList()
# llist.insert_at_end("A")
# llist.insert_at_end("B")
# llist.insert_at_end("C")
# llist.insert_at_end("D")
# llist.delete_at_start("A")
# print(llist.head.next.data)
# llist.insert_after_node(llist.head.next, "E")
# llist.swap_node("A", "C")
# llist.rev_list()
llist_1.sum_two_lists(llist_2)
llist_1.print_list()


