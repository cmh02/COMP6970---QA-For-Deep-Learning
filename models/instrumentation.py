"""
Instrumentation Model (Activation Probe)

This file implements an instrumentation model designed to extract intermediate
neuron activations from hidden layers of a neural network model.
It is based on lecture concepts for QA for Deep Learning.
"""

"""
LIBRARY IMPORT
"""

from collections.abc import Callable
import keras
from keras import layers


"""
MODEL DEFINITION
"""


class InstrumentationModel(keras.Model):
    """
    An instrumentation model (activation probe) that wraps a base neural network model
    and exposes the activations of its internal hidden layers as outputs.

    This model functions as a non-destructive probe: it does not alter the original
    classifier, but creates a multi-output functional model mapping the base model's
    inputs directly to the outputs of selected hidden layers (e.g., hidden Dense ReLU layers).
    """

    def __init__(
        self,
        model: keras.Model,
        name: str = "activation_probe",
        layer_filter: Callable[[layers.Layer], bool] | None = None,
        **kwargs,
    ):
        """
        Initialize the instrumentation model around a given base model.

        Args:
            model: The base Keras model to instrument.
            name: Name for the probe model container (default: 'activation_probe').
            layer_filter: Optional custom predicate function to filter layers.
                          If None, defaults to selecting all Dense layers excluding
                          the output layer (named 'predictions').
            **kwargs: Additional keyword arguments passed to keras.Model.
        """
        if layer_filter is None:
            hidden_layers = [
                layer
                for layer in model.layers
                if isinstance(layer, layers.Dense) and layer.name != "predictions"
            ]
        else:
            hidden_layers = [
                layer for layer in model.layers if layer_filter(layer)
            ]

        outputs = [layer.output for layer in hidden_layers]
        super().__init__(inputs=model.inputs, outputs=outputs, name=name, **kwargs)

        self.base_model = model
        self.hidden_layers = hidden_layers
