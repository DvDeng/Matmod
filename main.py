import math
from queue import PriorityQueue



class Station:
    def __init__(self, max_orders = 1, max_buffers=0):
        self.max_orders = max_orders
        self.max_buffers = max_buffers
        self.orders = []
        self.buffers = [] 

event_queue = PriorityQueue()

#nån loop för att generera ordrar


items = [1,2,3]
order = Order(items)
event_queue.put((2,order))









#slut


stations = [] 
order_queue = []

