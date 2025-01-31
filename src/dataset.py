

class Dataset:
    def __init__(self, bucket: str):
        self.bucket = bucket
        self.raw = pass
        self.cleaned = pass
        self.embeddings = pass
    
    '''
    processing text datasets reflecting game_states
    and player actions. Intent is an unsupervised 
    learning algorithm 