# estab.py

class ESTAB:

    def __init__(self):
        self.t = 0
        self.b = 0 
        self.array =[]
        

    def read_int_list(self):
        self.t = int(input())
        self.b = int(input())
        for val in range(self.b):
            self.array.append(int(input()))

        print(self.array)

    
if __name__ == "__main__":
    estb = ESTAB()
    estb.read_int_list()
