import math
from queue import PriorityQueue
from m import Order
import m
from random import randint

#time_to_get = [1 + 0.01 * x for x in range(1000)]
time_to_get = m.generate_time_to_get_list()

class Arrival:
    def __init__(self,item,station):
        self.item=item
        self.station=station
    

class Station:
    def __init__(self, max_orders = 1, max_buffers=0):
        self.max_orders = max_orders
        self.max_buffers = max_buffers
        self.orders = []
        self.buffers = []
        self.approching_items = []

#event_queue = m.generate_order_queue()



#nån loop för att generera ordrar











#slut


stations = [Station() for _ in range(10)]

t = 0
while not event_queue.empty():
    (t, event) = event_queue.get()
    if event.isinstance(Order):
        items = event.items
        best_station = None
        best_time = 10**9
        for station in stations:
            if len(station.orders)>=station.max_orders:
                continue
            time = 0
            for item in items:
                if item not in station.buffers and item not in station.approching_items:
                    time = max(time_to_get[item],time)
            if time < best_time:
                best_time = time
                best_station = station
        if best_station == None:
            event_queue.add((t+20,order))
            continue

        for i in range(len(items)-1,-1,-1):
            item = items[i] 
            if items in best_station.buffers:
                items.remove(item)
            elif item not in best_station.approching_items:
                event_queue.add((t+time_to_get[item],Arrival(item,station)))
                best_station.approching_items.append(item)
        
        if len(items)!=0:
            best_station.orders.append(order)
            #order done


    if event.isinstance(Arrival):
        Station: station = event.station
        item = event.station
        i=0
        while i < len(station.orders):
            order = station.orders[i]
            while item in order.items:
                order.remove(item)
            if len(order.items)==0:
                station.orders.remove(order)
                #order done
            i+=1
        while len(items) >= station.max_buffers:
            items.remove(randint(0,station.max_buffers))
        items.append(item)


print("total time:",t)


