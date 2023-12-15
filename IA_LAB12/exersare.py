import tensorflow as tf
class MyRNNCell(tf.keras.layers.Layer):
    def __init__(self,rnn_units,input_dim,output_dim):
        super(MyRNNCell,self).__init()
        self.W_xh=self.add_weight([rnn_units,input_dim])
        self.W_hh = self.add_weight([rnn_units, rnn_units])
        self.W_hy = self.add_weight([output_dim, rnn_units])

        self.h=tf.zeros([rnn_units,1])

    def call(self,x):
        self.h=tf.math.tanh(self.W_hh*self.h+self.W_xh*x)
        output=self.W_hy*self.h
        return output,self.h
