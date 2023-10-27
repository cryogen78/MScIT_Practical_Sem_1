class McCullochPittsNeuron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold
    def activate(self, inputs):
        if sum([x * w for x, w in zip(inputs, self.weights)]) >= self.threshold:
            return 1
        else:
            return 0
def ANDNOT(a, b):
    weights = [1, -1]
    threshold = 1
    neuron = McCullochPittsNeuron(weights, threshold)
    return neuron.activate([a, b])

print("ANDNOT(0, 0) =", ANDNOT(0, 0))
print("ANDNOT(0, 1) =", ANDNOT(0, 1))
print("ANDNOT(1, 0) =", ANDNOT(1, 0))
print("ANDNOT(1, 1) =", ANDNOT(1, 1))