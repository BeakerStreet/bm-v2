import tensorflow as tf
import sagemaker


class bmv2:
    def __init__(self):
        self.model = pass
        self.role = self.get_role()
        self.estimator = pass
    
    def get_role(self):
        return sagemaker.get_execution_role()
    

    '''
    Goal: predict the build orders and settle locations
    of players by difficulty with a clustering algorithm 
    organising actions and game states by t10 culture, 
    science, faith, and gold.
    '''