class AceValueError():
    
    def __init__(self, ace_value):
        self.ace_value = ace_value

        if ace_value != 11 and ace_value != 1: 
            return AceValueError