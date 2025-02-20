import random

class Species:
    def __init__(self, player):
        self.players = []
        self.avg_fitness = 0
        self.threshold = 1.2
        self.players.append(player)
        self.benchmark_fitness = player.fitness
        self.benchmark_brain = player.brain.copy()
        self.best = player.copy()
        self.staleness = 0

    def compare(self, brain):
        similarity = self.weight_diff(brain, self.benchmark_brain)
        return self.threshold > similarity

    @staticmethod
    def weight_diff(brain1, brain2):
        total_diff = 0
        for neuron1 in range(0, len(brain1.nodes)):
            for neuron2 in range(0, len(brain1.nodes)):
                if neuron1 == neuron2:
                    total_diff += abs(brain1.connections[neuron1].weight - brain2.connections[neuron2].weight)
        return total_diff


    def add_to_specs(self, player):
        self.players.append(player)

    def sort_by_fitness(self):
        self.players.sort(key= lambda x: x.fitness, reverse=True)

    def calc_avg_fitness(self):
        total_fitness = 0
        for player in self.players:
            total_fitness += player.fitness
        if self.players:
            self.avg_fitness = int(total_fitness / len(self.players))
        else:
            self.avg_fitness = 0


    def offspring(self):
        newborn = self.players[random.randint(1, len(self.players))-1].clone()
        newborn.brain.mutate()
        return newborn