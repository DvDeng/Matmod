from queue import PriorityQueue
from m import Order,generate_order_queue,generate_time_to_get_list
from simulator import Station,simulate


    

#Tiden det tar att hämta saker:
#time_to_get = [15 + 2 * x for x in range(10000)]
time_to_get = generate_time_to_get_list()



#Order Listan
#event_queue = generate_order_queue(100,5)
event_queue = PriorityQueue()

for x in range(20):
    event_queue.put((10*x,Order([100-x,95-x,90-x])))


#Stationerna
stations = [Station(5,2) for _ in range(1)]





#Simuleringen
time = simulate(event_queue,stations,time_to_get,debug=False)
print("Simulation took", time, "seconds")


