import lasagne
import numpy as np


import lasagne
import theano.tensor as T
import theano
from lasagne.nonlinearities import softmax
from lasagne.layers import InputLayer, DenseLayer, get_output
from lasagne.updates import nesterov_momentum
l_in = InputLayer((100, 20))
l1 = DenseLayer(l_in, num_units=3, nonlinearity=softmax)
x = T.matrix('x')  # shp: num_batch x num_features
y = T.ivector('y') # shp: num_batch
l_out = get_output(l1, x)
print(l_out)
params = lasagne.layers.get_all_params(l1)
print(params)
loss = T.mean(T.nnet.categorical_crossentropy(l_out, y))
print(loss)
updates = nesterov_momentum(loss, params, learning_rate=1e-4, momentum=.9)
train_fn = theano.function([x, y], updates=updates)


dee = l_out[T.arange(l_out.shape[0]), (1,)]
print(dee)