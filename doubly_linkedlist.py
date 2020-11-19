class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            new_node.next = None
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node

            cur = cur.next

    def add_before_node(self, key , data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev

            cur = cur.next

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self .head:
                # case 1
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    cur.prev = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key:
                # case 3:
                if cur.next is not None:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                # case 4:
                else:
                    prev = cur.prev
                    cur.prev = None
                    prev.next = None
                    cur = None
                    return
            cur = cur.next

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # case 1
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    cur.prev = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur == node:
                # case 3:
                if cur.next is not None:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                # case 4:
                else:
                    prev = cur.prev
                    cur.prev = None
                    prev.next = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self):
        temp = None
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev

    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur is not None:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

    def pairs_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs




dlist = Doubly_Linkedlist()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.append(5)
print(dlist.pairs_with_sum(10))
# dlist.remove_duplicates()
# dlist.reverse()
# dlist.delete(4)
# dlist.add_after_node(1, 11)
# dlist.add_before_node(2, 12)
dlist.print_list()
