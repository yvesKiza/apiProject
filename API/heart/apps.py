from django.apps import AppConfig
import numpy as np 
import joblib 
from django.conf import settings
import os


class HeartConfig(AppConfig):
    name = 'heart'
class Predictator(AppConfig):
  
    model_name='model.h5'
    scaler_name='scaler.pkl'
    model_path = os.path.join(settings.MODEL_ROOT, model_name)
    scaler_path = os.path.join(settings.MODEL_ROOT, scaler_name)
    model=joblib.load(model_path)
    scaler=joblib.load(scaler_path)
