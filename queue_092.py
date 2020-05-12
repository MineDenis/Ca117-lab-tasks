class Queue(object):

    def __init__(self):
        self.lis = []

    def enqueue(self, e):
        self.lis.append(e)

    def first(self):
        return self.lis[0]

    def is_empty(self):
        return len(self.lis) == 0

    def dequeue(self):
        return self.lis.pop(0)

    def __len__(self):
        return len(self.lis)
