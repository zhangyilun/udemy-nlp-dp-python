# class for lstm recurrent unit

import numpy as np
import theano
import theano.tensor as tensor

from util import init_weight


'''
3 gates: input, output, forget

input gate: Wxi, Whi, Wci, bi
forget gate: Wxf, Whf, Wcf, bf
candidate gate: Wxc, Whc, bc
output gate: Wxo Who, Wco, bo
'''

def LSTM:

	def __init__(self, Mi, Mo, activation):
		self.Mi = Mi
		self.Mo = Mo
		self.f = activation
		
		# input gate
		Wxi = init_weight(Mi, Mo)
		Whi = init_weight(Mo, Mo)
		Wci = init_weight(Mo, Mo)
		bi = np.zeros(Mo)
		# forget gate
		Wxf = init_weight(Mi, Mo)
		Whf = init_weight(Mo, Mo)
		Wcf = init_weight(Mo, Mo)
		bf = np.zeros(Mo)
		# cell
		Wxc = init_weight(Mi, Mo)
		Whc = init_weight(Mo, Mo)
		bc = np.zeros(Mo)
		# output gate
		Wxo = init_weight(Mi, Mo)
		Who = init_weight(Mo, Mo)
		Wco = init_weight(Mo, Mo)
		bo = np.zeros(Mo)
		# initial values
		c0 = np.zeros(Mo)
		h0 = np.zeros(Mo)

		self.Wxi = theano.shared(Wxi)
		self.Whi = theano.shared(Whi)
		self.Wci = theano.shared(Wci)
		self.bi = theano.shared(bi)
		self.Wxf = theano.shared(Wxf)
		self.Whf = theano.shared(Whf)
		self.Wcf = theano.shared(Wcf)
		self.bf = theano.shared(bf)
		self.Wxc = theano.shared(Wxc)
		self.Whc = theano.shared(Whc)
		self.bc = theano.shared(bc)
		self.Wxo = theano.shared(Wxo)
		self.Who = theano.shared(Who)
		self.Wco = theano.shared(Wco)
		self.bo = theano.shared(bo)
		self.c0 = theano.shared(c0)
		self.h0 = theano.shared(ho)
		self.params = [self.Wxi, self.Whi, self.Wci, self.bi,
		               self.Wxf, self.Whf, self.Wcf, self.bc,
		               self.Wxc, self.Whc, self.bc,
		               self.Wxo, self.Who, self.Wco, self.bo,
		               self.c0, self.h0]

    def recurrence(self, x_t, h_t1, c_t1):
    	i_t = T.nnet.sigmoid(x_t.dot(self.Wxi) + h_t1.dot(self.Whi) + c_t1.dot(self.Wci) + self.bi)
    	f_t = T.nnet.sigmoid(x_t.dot(self.Wxf) + h_t1.dot(self.Whf) + c_t1.dot(self.Wcf) + self.bf)
    	c_t = f_t * c_t1 + i_t * T.tanh(x_t.dot(self.Wxc) + h_t1.dot(self.Wci) + self.bi)
    	o_t = T.nnet.sigmoid(x_t.dot(self.Wxo) + h_t1.dot(self.Who) + c_t.dot(self.Wco) + self.bo)
    	h_t = o_t * T.tanh(c_t)
    	return h_t, c_t

    def output(self, x):
    	[h, c], _ = theano.scan(
    		fn = self.recurrence,
    		sequences = x,
    		outputs_info = [self.h0, self.c0],
    		n_steps = x.shape[0]
    	)
    	return h



