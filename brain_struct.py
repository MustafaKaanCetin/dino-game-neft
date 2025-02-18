import random
import math

class Brain:
    #Network
    def __init__(self, inputs, clone=False):
        self.synapses = []
        self.neurons = []
        self.inputs = inputs
        self.net = []
        self.layers = 2
        if not clone:
            # Input neurons
            for i in range(0, self.inputs):
                self.neurons.append(Neuron(i))
                self.neurons[i].layer = 0
            # Create bias neuron
            self.neurons.append(Neuron(3))
            self.neurons[3].layer = 0
            # Create output neuron
            self.neurons.append(Neuron(4))
            self.neurons[4].layer = 1
            # Create connections
            for i in range(0, 4):
                self.synapses.append(Synapse(self.neurons[i], self.neurons[4], random.uniform(-1, 1)))

    def connect_neurons(self):
        for i in range(0, len(self.neurons)):
            self.neurons[i].connections = []
        for i in range(0, len(self.synapses)):
            self.synapses[i].from_node.connections.append(self.synapses[i])

    def generate_net(self):
        self.connect_neurons()
        self.net = []
        for j in range(0, self.layers):
            for i in range(0, len(self.neurons)):
                if self.neurons[i].layer == j:
                    self.net.append(self.neurons[i])

    def feed_forward(self, vision):
        for i in range(0, self.inputs):
            self.neurons[i].output_value = vision[i]

        for i in range(0, len(self.net)):
            self.net[i].activate()

        output_value = self.neurons[self.inputs].output_value

        for i in range(0, len(self.neurons)):
            self.neurons[i].input_value = 0

        return output_value

    def clone(self):
        clone = Brain(self.inputs, True)
        for n in self.neurons:
            clone.neurons.append(n.clone())
        for s in self.synapses:
            clone.synapses.append(s.clone(clone.neurons[s.from_node.id], clone.neurons[s.to_node.id]))
        return clone

    def get_node(self, id_number):
        for n in self.neurons:
            if n.id == id_number:
                return n
        return None

    def mutate(self):
        if random.uniform(0, 1) < 0.1:
            for s in range(0, len(self.synapses)):
                self.synapses[s].mutate()


class Neuron:
    #Node
    def __init__(self, id_number):
        self.id = id_number
        self.layer = 0
        self.input_value = 0
        self.output_value = 0
        self.connections = []

    def activate(self):
        def sigmoid(x):
            return 1 / (1 + math.exp(-x))

        if self.layer == 1:
            self.output_value = sigmoid(self.input_value)

        for i in range(0, len(self.connections)):
            self.connections[i].to_node.input_value += \
                self.connections[i].weight * self.output_value

    def clone(self):
        clone = Neuron(self.id)
        clone.id = self.id
        clone.layer = self.layer
        return clone

class Synapse:
    #Connection
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def mutate(self):
        if random.uniform(0, 1) < 0.1:
            self.weight += random.uniform(1, 1)
        else:
            self.weight = random.gauss(-1, 1)/10
            if self.weight > 1:
                self.weight = 1
            elif self.weight < -1:
                self.weight = -1

    def clone(self, from_node, to_node):
        clone = Synapse(from_node, to_node, self.weight)
        return clone