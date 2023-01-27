from typing import List
from app.application.ml_model_trainers.base import BaseModelTrainer

def train_models(model_trainers: List[BaseModelTrainer]) -> None:
    for trainer in model_trainers:
        trainer.train_model()