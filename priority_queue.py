
import heapq


class PriorityQueue:
    def __init__(self) :
        self.elements =[]

    def is_empty(self):
        return not self.elements # if the list is empty then this will return true

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def __str__(self):
        return str(self.elements)
    

if __name__ == "__main__":
    pq= PriorityQueue()
    print(pq)
    print(pq.is_empty())
    # we are putting item and priority into the queue (item, priority)
    pq.put("eat",2)
    pq.put("swim",1)
    pq.put("drink",3)
    pq.put("walk",4)
    print(pq)
    print(pq.get()) # gets swim
    print(pq.get())# gets eat
    print(pq.get()) # gets drink
    print(pq) # this returns the 4th element which is walk 