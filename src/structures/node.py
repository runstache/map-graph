'''
Graph Node Class
'''

class Node:
    
    def __init__(self, id:str, type:str, data:dict):
        '''
        Constructor for a Node Type
        '''
        
        self.Id = id
        self.Type = type
        self.Data = data