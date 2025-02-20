import species
import conf
import dino
import operator
import math

class Population:
    def __init__(self, size):
        self.species_list = []
        self.players = []
        self.gen = 1
        self.size = size
        for i in range(self.size):
            self.players.append(dino.Dino())

    def update_players(self):
        for player in self.players:
            if player.alive:
                player.think()
                player.draw()
                player.update()
                player.survival_time += 1

    def natural_selection(self):
        self.speciate()
        self.calculate_fitness()
        # self.kill_extinct()
        self.kill_stale()
        self.sort_by_fitness()
        self.next_gen()

    def speciate(self):
        for s in self.species_list:
            s.players = []
        for p in self.players:
            add_to_species = False
            for s in self.species_list:
                if s.compare(p.brain):
                    s.add_to_specs(p)
                    add_to_species = True
                    break
            if not add_to_species:
                self.species_list.append(species.Species(p))

    def calculate_fitness(self):
        for p in self.players:
            p.calculate_fitness()

        for s in self.species_list:
            s.calc_avg_fitness()

    def kill_extinct(self):
        species_bin = []

        for s in self.species_list:
            if len(s.players) == 0:
                species_bin.append(s)

        for s in species_bin:
            self.species_list.remove(s)

    def kill_stale(self):
        species_bin = []
        players_bin = []

        for s in self.species_list:
            if s.staleness > 8:
                if len(self.species_list) > len(species_bin) + 1:
                    species_bin.append(s)
                    for p in s.players:
                        players_bin.append(p)

        for s in species_bin:
            self.species_list.remove(s)

        for p in players_bin:
            self.players.remove(p)

    def next_gen(self):
        children = []
        for s in self.species_list:
            children.append(s.best.copy())
        children_per_spec = math.floor((self.size - len(self.species_list)) / len(self.species_list))
        for s in self.species_list:
            for i in range(0, children_per_spec):
                children.append(s.offspring())

        while len(children) < self.size:
            children.append(self.species_list[0].offspring())
        self.players = []
        for child in children:
            self.players.append(child)
        self.gen += 1

    def sort_by_fitness(self):
        self.species_list.sort(key=lambda x: x.avg_fitness, reverse=True)

    def extinct(self):
        extinct = True

        for p in self.players:
            if p.alive:
                extinct = False
        return extinct

