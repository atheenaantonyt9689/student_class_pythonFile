class Student:
    def __init__(self,name,marks=[]):
        self.name=name
        self.marks=marks


    def average_marks(self): 
        sum1=sum(self.marks)
        length=len(self.marks)
        average1=sum1/length

        return average1


        
        
             

    def highest_marks(self):
        maximum1=max(self.marks)
        
        return maximum1
        


