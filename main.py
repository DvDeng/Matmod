import math
from queue import PriorityQueue
from m import Order
import m
from random import randint






class Arrival(m.Event):
    def __init__(self,item,station):
        self.item=item
        self.station=station
    
    def __str__(self):
        return "Arriival of item "+str(self.item)+" to station "+str(stations.index(self.station))
    

class Station:
    next_id=0
    def __init__(self, max_orders = 1, max_buffers=0, id=-1):
        self.max_orders = max_orders
        self.max_buffers = max_buffers
        self.orders = []
        self.buffers = []
        self.approching_items = []
        if id!=-1:
            self.id = id
        else:
            self.id = Station.next_id
            Station.next_id+=1
    
    def __str__(self):
        return("station: "+str(self.id))
    

#Tiden det tar att hämta saker:
time_to_get = [15 + 2 * x for x in range(1000)]
#time_to_get = m.generate_time_to_get_list()



#Order Listan
#event_queue = m.generate_order_queue()
event_queue = PriorityQueue()

for x in range(40):
    event_queue.put((10*x,Order([x,x+1,x+2])))




#Stationerna
stations = [Station(1,0) for _ in range(10)]





#Simuleringen

def handle_order(event):
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
        event_queue.put((t+20,event))
        return

    for i in range(len(items)-1,-1,-1):
        item = items[i] 
        if items in best_station.buffers:
            items.remove(item)
        elif item not in best_station.approching_items:
            event_queue.put((t+time_to_get[item],Arrival(item,best_station)))
            best_station.approching_items.append(item)
    
    if len(items)!=0:
        best_station.orders.append(event)
        print("Order going to ", best_station)
    else:
        print(stations.index(station), "done")



def handle_arrival(event):
    station = event.station
    item = event.item
    i=0
    while i < len(station.orders):
        order = station.orders[i]
        while item in order.items:
            order.items.remove(item)
        if len(order.items)==0:
            station.orders.remove(order)
            print(stations.index(station), "done")
        i+=1

    if station.max_buffers>0:
        items = station.buffers
        while len(items) >= station.max_buffers:
            items.remove(items[randint(0,station.max_buffers-1)])
        items.append(item)
    for order in station.orders:
        print("Remaining items: ",order.items)



t = 0
while not event_queue.empty() and t<2000:
    (t, event) = event_queue.get()
    print(t, event)

    if isinstance(event, Order):
        handle_order(event)


    if isinstance(event, Arrival):
        handle_arrival(event)


print("total time:",t)


