class data:
    def __init__(self,X,operation,freq=[],grped=True,):
        grped = self.grped
        operation = self.operation
        freq = self.freq
        if grped==False:
            X = self.X
        if grped==True:
            (upper,lower,class_intervel)= self.X
            if freq ==[]:
                print('input frequencies or it wouldnt work')
