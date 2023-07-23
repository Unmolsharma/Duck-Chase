class Duck:
    def __init__(self, n, w, s = "Eider"):
        self.name = n
        self.weight = w
        self.species = s
        self.x = 0
        self.y = 0
    

    def quack(self, n=1):
        for i in range(0,n):
            print("Quack")


    
