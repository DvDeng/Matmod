import math
class order:
    def __init__(self, items):
        self.items = items

class station:
    def __init__(self, max_orders = 1, max_buffers=0):
        self.max_orders = max_orders
        self.max_buffers = max_buffers
        self.orders = []
        self.buffers = [] 
    


time_to_get = [1+0.01*x for x in range(1000)] 
number_of_pallets = [10]*1000

stations = [] 
order_queue = []

