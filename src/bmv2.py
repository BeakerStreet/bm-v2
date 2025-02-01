import tensorflow as tf
import sagemaker
from sagemaker.amazon.amazon_estimator import KMeans

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
