from tensorflow.keras import Model
from app.core.constants.ml_model_metrics import METRICS as metrics
from keras.backend import eval

class PredictionPrecisionCalculator(object):

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_prediction_precision(model: Model) -> float:        
        model.compile(metrics = metrics)
        
        return eval(model.compiled_metrics._metrics[1].result())
