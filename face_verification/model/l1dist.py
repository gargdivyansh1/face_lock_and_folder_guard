import tensorflow as tf

class L1Dist(tf.keras.layers.Layer): #type: ignore
    def __init__(self, **kwargs):
        super().__init__()

    def call(self, inputs, **kwargs):
        input_embedding, validation_embedding = inputs
        return tf.math.abs(input_embedding - validation_embedding)
