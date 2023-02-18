import math
from queue import PriorityQueue
from m import Order
import m
from random import randint




time_to_get = [15 + 2 * x for x in range(1000)]
#time_to_get = m.generate_time_to_get_list()

class Arrival(m.Event):
    def __init__(self,item,station):
        self.item=item
        self.station=station
    
    def __str__(self):
        return "item: "+str(self.item)+" station: "+str(stations.index(self.station))
    

class Station:
    def __init__(self, max_orders = 1, max_buffers=0):
        self.max_orders = max_orders
        self.max_buffers = max_buffers
        self.orders = []
        self.buffers = []
        self.approching_items = []
    
#event_queue = m.generate_order_queue()
event_queue = PriorityQueue()
for x in range(30):
    event_queue.put((10*x,Order([x,x+1,x+2])))

#nån loop för att generera ordrar











#slut


stations = [Station() for _ in range(10)]

t = 0


#while not event_queue.empty():
 #   (t,event) = event_queue.get()
  #  print(t,event)
while not event_queue.empty() and t<200:
    (t, event) = event_queue.get()
    print(t, event)
    if isinstance(event, Order):
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
            event_queue.put((t+20,order))
            continue

        for i in range(len(items)-1,-1,-1):
            item = items[i] 
            if items in best_station.buffers:
                items.remove(item)
            elif item not in best_station.approching_items:
                event_queue.put((t+time_to_get[item],Arrival(item,station)))
                best_station.approching_items.append(item)
        
        if len(items)!=0:
            best_station.orders.append(event)
        else:
            print(stations.index(station), "done")



    if isinstance(event, Arrival):
        Station: station = event.station
        item = event.station
        i=0
        while i < len(station.orders):
            order = station.orders[i]
            while item in order.items:
                order.remove(item)
            if len(order.items)==0:
                station.orders.remove(order)
                print(stations.index(station), "done")
            i+=1
        if station.max_buffers>0:
            while len(items) >= station.max_buffers:
                items.remove(items[randint(0,station.max_buffers-1)])
            items.append(item)
        for order in station.orders:
            print order.items


print("total time:",t)


