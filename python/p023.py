#Use a heap to keep track of the minimal no
#the size of the heap:k
#Time: O(nlogk)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Heap(object):
    def __init__(self, x):
        self.heap = [x]
        self.size = 1
    def swap(self, x, y):
        return y, x
    def insert(self, x):
        if self.size == len(self.heap):
            self.heap.append(x)
        else:
            self.heap[self.size] = x
        self.size += 1
        i = self.size-1
        while i > 0 and self.heap[i].val < self.heap[(i-1)/2].val:
            self.heap[i], self.heap[(i-1)/2] = self.swap(self.heap[i], self.heap[(i-1)/2])
            i = (i-1)/2
    def popRoot(self):
        rt = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        i = 0
        while i*2+1 < self.size:
            j1 = i*2+1; j2 = j1+1
            if j2 < self.size and self.heap[j2].val < self.heap[j1].val:
                j1 = j2
            if self.heap[i].val > self.heap[j1].val:
                self.heap[i], self.heap[j1] = self.swap(self.heap[i], self.heap[j1])
                i = j1
            else:
                break
        return rt
    def isEmpty(self):
        return self.size == 0
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        mylist = [l for l in lists if l != None]
        if mylist == []:
            return None
        heap = Heap(mylist[0])
        for i in range(1, len(mylist)):
            heap.insert(mylist[i])
        h = None
        while not heap.isEmpty():
            p = heap.popRoot()
            if h == None:
                h = p
            else:
                last.next = p
            last = p
            if p.next != None:
                heap.insert(p.next)
        return h