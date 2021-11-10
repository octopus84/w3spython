#!/usr/bin/python

#red neuronal con Tensorflow
import tensorflow as tf
import numpy as np

celsius= np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit= np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

#framework keras
#permite programar red neuronal rapida

# capa tipo Densa ,  
# units =1 : Neuronas de la capa
# input_shape=[1] : Una variable de entrada, con una Neurona
capa = tf.keras.layers.Dense(units =1, input_shape=[1]) 
#modelo de capa
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0,1),
    loss= 'mean_squared_error'
)

print("Comienza entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs =1000, verbose=False)
print("Entrenamiento Terminado!!!")