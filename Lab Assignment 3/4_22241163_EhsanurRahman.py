import numpy as np

f = open("input.txt", "r")
n, target = f.readline().split()
n, target = int(n), int(target)

batsman = []
avg_run = []
for i in range(n):
    name, run = f.readline().split()
    batsman.append(name)
    avg_run.append(int(run))

print(batsman)


def fitness(population, n):
    fitness = np.zeros(len(population))
    for i in range(len(population)):
        for j in range(n):
            if population[i][j] == 1:
                fitness[i] += avg_run[j]
    return fitness


def select(population, fit):
    a = np.arange(len(population))
    p = fit / np.sum(fit)
    return np.random.choice(a, 2, replace=True, p=p)


def crossover(x, y):
    n = len(x)
    c = np.random.randint(0, n)
    return np.append(x[:c], y[c:])


def mutate(x, mutation_threshold):
    n = len(x)
    for i in range(n):
        if np.random.random() <= mutation_threshold:
            x[i] = 1 - x[i]
    return x


def GA(population, n, mutation_threshold):
    count = 0
    while count < 250:
        count += 1
        Q = np.zeros((len(population), n))
        for i in range(len(population) // 2):
            x, y = select(population, fitness(population, n))
            z = crossover(population[x], population[y])
            w = mutate(z, mutation_threshold)
            Q[i] = w
        population = Q
        fit = fitness(population, n)
        if target - 60 < np.max(fit) < target + 70:
            if np.max(fit) == target:
                result = ""
                for i in population[np.argmax(fit)]:
                    result += str(int(i))
                return result
    return -1


start_population = 8
mutation_threshold = 0.3
population = np.random.randint(0, 2, (start_population, n))
print(GA(population, n, mutation_threshold))
