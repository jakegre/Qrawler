class PriorityQueue:
    def __init__(self):
        self.__qlist = []
    def insert(self, item):
        self.__qlist.append(item)
    def remove(self):
        """
        Removes the item of highest priority
        (this is the max item in the PQ)
        """
        if not self.empty():
            m = max(self.__qlist)
            self.__qlist.remove(m)
            return m
    def highest(self):
        if not self.empty():
            return max(self.__qlist)
    def empty(self):
        return len(self.__qlist) == 0
    def size(self):
        return len(self.__qlist)

    def __str__(self):
        p = "Priority Queue: \n"
        for i in self.__qlist:
            p += str(i)
        return p
