class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def main():
    q = Queue()

    print("Is the queue empty?", q.is_empty())  # Should print True

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Size of the queue:", q.size())  # Should print 3
    print("Dequeue item:", q.dequeue())  # Should print 10
    print("Size of the queue after dequeue:", q.size())  # Should print 2

if __name__ == "__main__":
    main()
