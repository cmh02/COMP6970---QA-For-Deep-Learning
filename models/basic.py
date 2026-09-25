"""
Basic Neural Network Model

This file creates a basic neural network for use in in-class examples.
It is based on the provided details from lectures given for QA for Deep Learning.
"""

"""
LIBRARY IMPORT
"""

import keras
from keras import layers


"""
MODEL DEFINITION
"""


class BasicNeuralNetwork(keras.Sequential):
    """
    A reusable basic feedforward neural network model using Keras Sequential.

    Architecture:
        - Input: shape (28, 28)
        - Flatten: flattens 2D input (28x28) into a 1D vector (784) (name: 'flatten')
        - Dense: 64 units, ReLU activation (name: 'dense_64')
        - Dense: 32 units, ReLU activation (name: 'dense_32')
        - Dense: 10 units, Softmax activation (name: 'predictions')
    """

    def __init__(
        self,
        input_shape: tuple[int, ...] = (28, 28),
        num_classes: int = 10,
        name: str | None = None,
        **kwargs,
    ):
        """
        Initialize the BasicModel with the sequential architecture.

        Args:
            input_shape: Shape of the input images/tensors (default: (28, 28)).
            num_classes: Number of output prediction classes (default: 10).
            name: Optional name for the Sequential model container.
            **kwargs: Additional keyword arguments passed to keras.Sequential.
        """
        model_layers = [
            keras.Input(shape=input_shape),
            layers.Flatten(name="flatten"),
            layers.Dense(64, activation="relu", name="dense_64"),
            layers.Dense(32, activation="relu", name="dense_32"),
            layers.Dense(num_classes, activation="softmax", name="predictions"),
        ]
        super().__init__(layers=model_layers, name=name, **kwargs)