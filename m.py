import random

class Order:
    def __init__(self, items):
        self.items = items

 time_to_get = [60+0.6*x for x in range(1000)]

#nån fördelning av tid att hämta varor

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
                result.append(time_to_get[j])
                break
    return result

time_to_get = [1 + 0.01 * x for x in range(1000)]

# Generate a list of probabilities that follow the Pareto distribution
n = len(time_to_get)
alpha = 1.16
probabilities = [0] * n
for i in range(n):
    probabilities[i] = (i + 1) ** (-alpha) / sum(j ** (-alpha) for j in range(1, n + 1))

# Use the probabilities to sample 20 items from the time_to_get list
pareto_sample = sample_pareto(probabilities, 20)
