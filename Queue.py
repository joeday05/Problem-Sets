class Queue(object):
    def __init__(self):
        self.queue = []
        
    def __str__(self):
       return str(self.queue) 
    
    def insert(self, e):
        if type(e) == int:
            #self.queue.append(e)
            self.queue = [e] + self.queue
        else:
            print str(e) + ' is not an integer'
        
    def remove(self):
        try:
            #self.queue.reverse()
            e2 = self.queue.pop()
            #self.queue.reverse()
            return e2
        except:
            raise ValueError('the queue is empty')

    

queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove()
queue.insert(7)
print queue.remove()
print queue.remove()
#print queue.remove()

    
    