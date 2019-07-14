import numpy as np
import scipy.special

class NN:
  def __init__(self, n0, n1, n2):
    self.n0, self.n1, self.n2 = n0, n1, n2
  def activation(self, inputs): return scipy.special.expit(inputs)
  
  def train(self, inputs, targets):
    outputs2 = self.query(inputs)
    self.w1 += (targets-outputs2)*np.dot(outputs2*(1.0-outputs2), np.transpose(outputs1))*self.lr
    self.w0 += (targets-outputs1)*np.dot(outputs1*(1.0-outputs1), np.transpose(inputs))*self.lr

  def trains(self, inputs):
    for input in inputs: self.train(inputs, inputs([0]))
    
  def query(self, inputs):
    inputs0 = np.array(inputs, ndmin=2).T
    inputs1 = self.w0*inputs0
    outputs1 = self.activation(inputs1)
    inputs2 = self.w1*inputs1
    outputs2 = self.activation(inputs2)
    
with f,t=open('data.csv','r'), open('test.csv','r'):
  lines,tests = f.read_lines(),t.read_lines()
ai = NN(764, 100, 10)
ai.trains(lines)
print(ai.query(tests[0]))
