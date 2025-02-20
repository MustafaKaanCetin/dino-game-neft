import math
import random
import operator

class Brain:
    def __init__(self, input_nodes, clone=False):
        self.input_nodes = input_nodes
        self.output_nodes = 2
        self.layers = 3
        self.nodes = []
        self.connections = []
        self.net = []
        if not clone:
            for i in range(self.input_nodes):
                self.nodes.append(Node(i))
                self.nodes[i].layer = 0

            hidden_nodes = 5
            for i in range(self.input_nodes, self.input_nodes + hidden_nodes):
                self.nodes.append(Node(i))
                self.nodes[i].layer = 1

            for i in range(self.output_nodes):
                self.nodes.append(Node(i + self.input_nodes + hidden_nodes))
                self.nodes[i + self.input_nodes + hidden_nodes].layer = 2

            for i in range(self.input_nodes):
                for j in range(self.input_nodes, self.input_nodes + hidden_nodes):
                    self.connections.append(Connection(self.nodes[i], self.nodes[j], random.uniform(-1, 1)))

            for i in range(hidden_nodes):
                for j in range(self.output_nodes):
                    self.connections.append(Connection(self.nodes[i + self.input_nodes], self.nodes[j + self.input_nodes + hidden_nodes], random.uniform(-1, 1)))

    def connect(self):
        for i in range(0, len(self.nodes)):
            self.nodes[i].connections = []
        for i in range(0, len(self.connections)):
            self.connections[i].before.connections.append(self.connections[i])

    def generate_net(self):
        self.connect()
        self.net = []
        for j in range(0, self.layers):
            for i in range(0, len(self.nodes)):
                if self.nodes[i].layer == j:
                    self.net.append(self.nodes[i])

    def feed_forward(self, dino):
        input_list = dino.inputs()
        for i in range(0, len(input_list)):
            self.nodes[i].output = input_list[i]

        for i in self.net:
            i.act_func()

        output_values = [node.output for node in self.nodes if node.layer == 2]

        for node in self.nodes:
            node.input = 0

        return output_values

    def mutate(self):
        if random.uniform(0, 1) < 0.8:
            for i in range(0, len(self.connections)):
                self.connections[i].mutate()

    def get_node(self, id_num):
        for node in self.nodes:
            if node.id == id_num:
                return node

    def copy(self):
        copy = Brain(self.input_nodes, True)
        for i in self.nodes:
            copy.nodes.append(i.copy())
        for i in self.connections:
            copy.connections.append(i.copy(copy.get_node(i.before.id), copy.get_node(i.after.id)))
        copy.layers = self.layers
        copy.connect()
        return copy

class Node:
    def __init__(self, id_num):
        self.id = id_num
        self.input = 0
        self.output = 0
        self.layer = 0
        self.connections = []

    def act_func(self):
        def sigmoid(x):
            return 1 / (1 + math.exp(-x))

        def tanh_method(x):
            return math.tanh(x)

        if self.layer != 0:
            self.output = tanh_method(self.input)

        for i in range(0, len(self.connections)):
            self.connections[i].after.input += self.output * self.connections[i].weight

    def copy(self):
        copy = Node(self.id)
        copy.id = self.id
        copy.layer = self.layer
        return copy


class Connection:
    def __init__(self, before, after, weight):
        self.before = before
        self.after = after
        self.weight = weight

    def mutate(self):
        if random.uniform(0, 1) < 0.1:
            self.weight = random.uniform(-1, 1)
        else:
            self.weight = random.gauss(-1, 1)/10
            if self.weight > 1:
                self.weight = 1
            if self.weight < -1:
                self.weight = -1

    def copy(self, before, after):
        copy = Connection(before, after, self.weight)
        return copy