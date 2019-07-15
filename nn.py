import numpy as np
import math

class NN:
  def __init__(self, n0, n1, n2):
    self.n0, self.n1, self.n2 = n0, n1, n2
    self.w0 = np.random.normal(0.0, n1**-0.5, (n1, n0))
    self.w1 = np.random.normal(0.0, n2**-0.5, (n2, n1))
  def activation(self, inputs): return 1.0/(1.0-math.e**-inputs)
  
  def train(self, inputs, targets):
    outputs2 = self.query(inputs)
    self.w1 += (targets-outputs2)*np.dot(outputs2*(1.0-outputs2), np.transpose(outputs1))*self.lr
    self.w0 += (targets-outputs1)*np.dot(outputs1*(1.0-outputs1), np.transpose(inputs))*self.lr

  def trains(self, inputs):
    for input in inputs: self.train(inputs, inputs([0]))
    
  def query(self, inputs):
    inputs0 = np.array(inputs, ndmin=2).T
    inputs1 = np.dot(self.w0, inputs0)
    outputs1 = self.activation(inputs1)
    inputs2 = self.w1*inputs1
    outputs2 = self.activation(inputs2)
    
f=open('a.txt','r')
inputs = f.readlines()
f.close
ai = NN(784, 100, 10)

line = np.asfarray(inputs[0].split(',')[1:])#.reshape((28,28))
#ai.query(line)
#print(ai.query(tests[0]))
print(np.array([1,2,3,4,5,6], ndmin=))
