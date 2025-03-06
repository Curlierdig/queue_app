class queue:
    def __init__(self):
        self.queue = []
        self.waitlist = []

    def enqueue(self, item):
        if len(self.queue) < 10:
            self.queue.append(item)
        else:
            self.waitlist.append(item)

    def dequeue(self):
        #remove from queue and add to queue from waitlist if not empty
        if len(self.queue) > 0:
            self.queue.pop(0)
            if len(self.waitlist) > 0:
                self.queue.append(self.waitlist.pop(0))

    def peek(self):
        #return the next item in the queue
        if len(self.queue) == 0:
            return "queue is empty"
        else:
            return self.queue[0]
    
    def waitlistLength(self):
        #return the length of the waitlist
        return len(self.waitlist)
    
    def showQueue(self):
        #return the queue
        return self.queue
    

