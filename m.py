from queue import PriorityQueue
import random
#import matplotlib.pyplot as plt
random.seed(1)

#test

class Event():
    def __lt__ (self,other):
        return True

class Order(Event):
    def __init__(self, items, times_resent = 0):
        self.items = items
        self.times_resent = times_resent
    
    def __str__(self):
        return "order items: "+str(self.items)


# nån fördelning av tid att hämta varor

def sample_pareto(probabilities, k):
    cumulative_probability = 0
    pareto_probabilities = []
    for i, p in enumerate(probabilities):
        cumulative_probability += p
        pareto_probabilities.append(cumulative_probability)

    result = []
    for i in range(k):
        r = random.random()
        for j, p in enumerate(pareto_probabilities):
            if r <= p:
                result.append(order_list[j])
                break
    return result

nbr_unique_items = 1000
order_list = [0 + x for x in range(nbr_unique_items)]

nbrItemsInOrder = random.randint(1, 20)
    # Generate a list of probabilities that follow the Pareto distribution
n = len(order_list)
alpha = 1.16
probabilities = [0] * n
for i in range(n):
    probabilities[i] = (i + 1) ** (-alpha) / sum(j ** (-alpha)
                                                for j in range(1, n + 1))

# Use the probabilities to sample 20 items from the time_to_get list
pareto_sample = sorted(set(sample_pareto(probabilities, nbrItemsInOrder)))
sample = [sample_pareto(probabilities, nbr_unique_items)]

print(nbrItemsInOrder)
print(pareto_sample)
#plt.hist(sample, bins=n, density=True, cumulative=False)


#plt.show()


def generate_order_queue(nbr_orders=25, max_order_size=20, seed=1):
    random.seed(seed)
    order_queue = PriorityQueue() #contains tuples on the form (time, order)
    for i in range(nbr_orders):
        nbrItems = random.randint(1, max_order_size)
        orderList = sample_pareto(probabilities, nbrItems)
        order = Order(orderList)
        time = i*20
        order_queue.put((time, order))

    #lägg till element
    return order_queue

#q = generate_order_queue()
#while not q.empty():
#    t,o = q.get()
#    print(t,o)


def generate_time_to_get_list():
    #10% most used articles, 1 min retrieval time
    #30% second most used articles, 3 min retrieval time
    #60% third most used articles, 7 min retrieval time
    # time_to_get = [420]*nbr_unique_items
    time_to_get_10 = [60 for x in range(1*nbr_unique_items//10)]
    time_to_get_30 = [180 for x in range(3*nbr_unique_items//10)]
    time_to_get_60 = [420 for x in range(6*nbr_unique_items//10)]
    time_to_get = time_to_get_10 + time_to_get_30 + time_to_get_60
    assert(len(time_to_get)==nbr_unique_items)
    return time_to_get