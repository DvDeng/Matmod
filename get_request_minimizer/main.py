from generators import generate_order_queue
buffer_max = 3
parallel_orders = 3
order_count = 10000

def handle(order_list,look_ahead=20):
    
    buffer = [-1]*buffer_max
    get_count=0
    curr_orders = order_list[:min(parallel_orders,len(order_list))]
    i = parallel_orders
    unused_buffer_count = 0
    #print(order_list)
    while curr_orders:
        next_order=[]
        while i<len(order_list) and not next_order:
            next_order = order_list[i]
            i+=1
        
            for buffered_item in buffer:
                while buffered_item in next_order:
                    next_order.remove(buffered_item)

        if next_order:
            curr_orders.append(next_order)


        

        while curr_orders[0]:
            item = curr_orders[0][0]

            first_seen = [10**9]*len(buffer)
            #print(item)
        
            for buffer_index,buffered_item in enumerate(buffer): 
                index = i
                while index<min(i+look_ahead+1,len(order_list)):
                    if buffered_item in order_list[index]:
                        first_seen[buffer_index] = index
                        break
                    index+=1
            
            unused = first_seen.index(max(first_seen))
            
            buffer[unused]=item
            get_count+=1
            for order in curr_orders:
                while item in order:
                    order.remove(item)
        
        curr_orders.pop(0)
        #print("hej")
    #print("get_count:",get_count)
    return get_count


order_list = list(map(sorted,generate_order_queue(nbr_orders=10000)))
#print(order_list)
print("Buffer Max:",buffer_max,"\nParallel orders:",parallel_orders,"\nOrder count:",10000)
print("Random:", handle([x.copy() for x in order_list]))
print("Sort:", handle(sorted(order_list)))



        
        
                





