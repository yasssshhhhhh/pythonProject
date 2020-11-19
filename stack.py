class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        print(self.items)

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]


def rev_string(input_string):
    for i in range(len(input_string)):
        s.push(input_string[i])

    rev = ""
    while not s.is_empty():
        rev += s.pop()
    return rev


s = Stack()
input = "yashu"
# print(input_string[::-1])
print(rev_string(input))
