import tensorflow as tf
import sagemaker

class bmv2:
    def __init__(self, bucket):
        self.role = self.get_role()
        self.bucket = bucket
        self.model = None
    
    def get_role(self):
        return sagemaker.get_execution_role()
    
    def get_model(self):
        pass