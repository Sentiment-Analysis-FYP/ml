from django.apps import AppConfig
import html
from pathlib import Path
import os


class WebAppConfig(AppConfig):
    name = 'ml'
    MODEL_PATH = Path("models")
    BERT_PRETRAINED_PATH = Path("models/")