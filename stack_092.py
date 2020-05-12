class Stack(object):

    def __init__(self):
        self.lis = []

    def push(self, e):
        self.lis.append(e)

    def pop(self):
        return self.lis.pop()

    def top(self):
        return self.lis[-1]

    def is_empty(self):
        return len(self.lis) == 0

    def __len__(self):
        return len(self.lis)
