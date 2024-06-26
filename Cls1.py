#Making a Module with the name Cls
class Math(object):
    def __init__(self,a,b):
        self.A=a
        self.B=b
    def disp(self):
        p=self.A*self.B
        print("The Product of Two Numbers:",p)

