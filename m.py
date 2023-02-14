from queue import PriorityQueue
import random
import matplotlib.pyplot as plt
random.seed(1)

class Order:
    def __init__(self, items):
        self.items = items


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

nbrItemsInOrder=  random.randint(1, 20)

    
    

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
plt.hist(sample, bins=n, density=True, cumulative=False)


plt.show()

def generate_order_queue():
    order_queue = PriorityQueue() #contains tuples on the form (time, order)
    #lägg till element
    return order_queue

def generate_time_to_get_list():
    time_to_get = []
    return time_to_get()