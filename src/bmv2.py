import tensorflow as tf
from sagemaker import KMeans


    '''
    Goal: predict the build orders and settle locations
    of players by difficulty with a clustering algorithm 
    organising actions and game states by t10 culture, 
    science, faith, and gold.
    '''

class bmv2:
    def __init__(self, bucket):
        self.role = self.get_role()
        self.bucket = bucket
        self.model = None
        self.estimator = None
    
    def get_role(self):
        return sagemaker.get_execution_role()
    
    def get_model(self):
        # Initialize the KMeans estimator
        model = KMeans(role=self.role,
                        instance_count=1,
                        instance_type='ml.m4.xlarge',
                        k=num_clusters)

        self.model = model
        
        return model
