import scipy.special, numpy as np

class neuralNetwork:
  def __init__(self, n0, n1, n2, learningrate):
    self.n0, self.n1, self.n2, self.lr = n0, n1, n2, learningrate
    self.w0 = np.random.normal(0.0, n0**-0.5, (self.n1, self.n0))
    self.w1 = np.random.normal(0.0, n1**-0.5, (self.n2, self.n1))
    self.activation = lambda x: scipy.special.expit(x)

  def train(self, inputs_list, targets_list):
    inputs0 = np.array(inputs_list, ndmin=2).T
    targets = np.array(targets_list, ndmin=2).T
    outputs2, outputs1 = self.query(inputs_list)

    self.w1 += self.lr * np.dot(((targets - outputs2) * outputs2 * (1.0 - outputs2)), np.transpose(outputs1))
    self.w0 += self.lr * np.dot((np.dot(self.w1.T, targets - outputs2) * outputs1 * (1.0 - outputs1)), np.transpose(inputs0))

  def query(self, inputs):
    inputs0 = np.array(inputs, ndmin=2).T
    outputs1 = self.activation(np.dot(self.w0, inputs0))
    outputs2 = self.activation(np.dot(self.w1, outputs1))
    return outputs2, outputs1

output_nodes = 10
n =neuralNetwork(784,100,output_nodes, 0.3)

f = open('train.csv','r')
train = f.readlines()
f.close()
for e in range(5):
  for record in train:
    allvalues = record.split(',')
    inputs = (np.asfarray(allvalues[1:])/255.0*0.99)+0.01
    targets = np.zeros(output_nodes)+0.01
    targets[int(allvalues[0])]=0.99
    n.train(inputs, targets)

f = open('test.csv','r')
test = f.readlines()
f.close()
for record in test:
  allvalues = record.split(',')
  inputs = (np.asfarray(allvalues[1:])/255.0*0.99)+0.01
  print(allvalues[0], np.argmax(n.query(inputs)[0]))
