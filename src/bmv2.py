import tensorflow as tf
import sagemaker
from pydantic import BaseModel
from openai import OpenAI

class bmv2:
    def __init__(self):
        pass

class Behaviours(BaseModel):
    '''
    Pydantic model for behaviour data
    '''

    def __init__(self):
        
        self.pseudo_yields = {
            "PSEUDOYIELD_UNIT_SETTLER": float,
            "PSEUDOYIELD_CITY_BASE": float,
            "PSEUDOYIELD_UNIT_EXPLORER": float,
            "PSEUDOYIELD_CLEAR_BANDIT_CAMPS": float,
            "PSEUDOYIELD_TECHNOLOGY": float,
            "PSEUDOYIELD_CIVIC": float,
        }