import math


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

# challenge one, balance parenthesis


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string(index)

        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False

# 2 Reverse a string


def reverse_string(stac, reverse_string):
    for i in range(len(reverse_string)):
        stac.push(reverse_string[i])

    rev_str = ""
    while not stac.is_empty():
        rev_str += stac.pop()

    return rev_str


s = Stack()

print(reverse_string(s, 'kelvin'))

# convert decimal interger to binary


def divider(decimal):
    stac = Stack()

    while decimal != 0:
        remainder = decimal % 2
        stac.push(remainder)
        decimal = decimal // 2

    bin_num = ""
    while not stac.is_empty():
        bin_num += str(stac.pop())

    return bin_num


print(divider(242))
