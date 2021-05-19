class Queue:
    def __init__(self):
        self.queue = []
        self.count = 0

    def Enqueue(self, val):
        self.queue.append(val)
        self.count += 1

    def Dequeue(self):
        if self.count > 0:
            val = self.queue[0]
            self.queue.pop(0)
            self.count -= 1
            return val
        else:
            print("Empty queue")
            return None

    def Print(self):
        print(self.queue)

if __name__ == "__main__":
    queue = Queue()
    queue.Enqueue(1)
    queue.Enqueue(2)
    queue.Enqueue(3)
    queue.Print()
    queue.Dequeue()
    queue.Print()
    queue.Dequeue()
    queue.Print()
    queue.Dequeue()
    queue.Print()
    queue.Dequeue()

