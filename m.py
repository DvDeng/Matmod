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

order_list = [0 + x for x in range(1000)]

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
sample = [sample_pareto(probabilities, 1000)]

print(nbrItemsInOrder)
print(pareto_sample)
#plt.hist(sample, bins=n, density=True, cumulative=False)


#plt.show()


def generate_order_queue():
    order_queue = PriorityQueue() #contains tuples on the form (time, order)
    for i in range(25):
        nbrItems = random.randint(1, 20)
        orderList = []
        for i in range(0,5):
            l = random.randint(1, n)
            orderList.append(l)
        order = Order(orderList)
        time = i*20
        order_queue.put((time, order))

    #lägg till element
    return order_queue

print(generate_order_queue())

def generate_time_to_get_list():
    time_to_get = []
    return time_to_get()