import m
from random import randint

count = 0


class Arrival(m.Event):
    def __init__(self,item,station):
        self.item=item
        self.station=station
    
    def __str__(self):
        return "Arrival of item "+str(self.item)+" to "+str(self.station)
    

class Station:
    next_id=0
    def __init__(self, max_orders = 1, max_buffers=0, id=-1):
        self.max_orders = max_orders
        self.max_buffers = max_buffers
        self.orders = []
        self.buffers = []
        self.approacing_items = []
        if id!=-1:
            self.id = id
        else:
            self.id = Station.next_id
            Station.next_id+=1
    def __str__(self):
        return("station "+str(self.id))

def handle_order(event,event_queue,stations,time_to_get,current_time):
    items = event.items
    best_station = None
    best_time = 10**9
    for station in stations:
        #print(station.buffers)
        if len(station.orders)>=station.max_orders:
            continue
        time = 0
        for item in items:
            if item not in station.buffers and item not in station.approacing_items:
                time = max(time_to_get[item],time)
        if time < best_time:
            best_time = time
            best_station = station
    if best_station == None:
        event_queue.put((current_time+50,event))
        event.times_resent+=1
        global count
        count+=1
        return

    for i in range(len(items)-1,-1,-1):
        item = items[i] 
        if item in best_station.buffers:
            items.remove(item)
        elif item not in best_station.approacing_items:
            event_queue.put((current_time+time_to_get[item],Arrival(item,best_station)))
            best_station.approacing_items.append(item)
    
    if len(items)!=0:
        best_station.orders.append(event)
        #print("Order going to ", best_station)
    else:
        #print(stations.index(station), "done")
        pass


def handle_arrival(event,event_queue,stations):
    station = event.station
    item = event.item
    station.approacing_items.remove(item)
    i=0
    while i < len(station.orders):
        order = station.orders[i]
        while item in order.items:
            order.items.remove(item)
        if len(order.items)==0:
            station.orders.remove(order)
        i+=1

    if station.max_buffers>0:
        items = station.buffers
        while len(items) >= station.max_buffers:
            items.remove(items[randint(0,station.max_buffers-1)])
        items.append(item)
    for order in station.orders:
        pass

def simulate(event_queue, stations, time_to_get_list, debug = False):
    t = 0
    for station in stations:
        station.buffers = []
        station.orders = []
        station.approacing_items = []

    while not event_queue.empty(): #and t<20000:
        (t, event) = event_queue.get()
        if debug:
            print(t, event)

        if isinstance(event, m.Order):
            handle_order(event,event_queue,stations,time_to_get_list,t)


        if isinstance(event, Arrival):
            handle_arrival(event,event_queue,stations)
    return t