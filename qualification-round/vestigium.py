# p5.py
import numpy as np

class vestiginum:

    def __init__(self, arr=np.array):
        self.arr =  arr

    def print_matrix(self):
        print(self.arr)

    def trace(self):
        trace = 0
        r = 0
        c = 0
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[0]):
                if i == j:
                    trace += self.arr[i][j] #sum of diagnal elements
            if len(set(self.arr[:, i])) != self.arr.shape[0]: 
                c += 1  
            if len(set(self.arr[i, :])) != self.arr.shape[0]:
                r += 1
        print(trace, r, c)
           
if __name__ == "__main__":
    seq1 = np.array([2, 2, 2, 2, 2, 3, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2]).reshape((4,4)) 
    seq2 = np.array([2, 1, 3, 1, 3, 2, 1, 2, 3]).reshape((3,3)) 
    seq3 = np.array([1, 2, 3, 4, 2, 1, 4,3, 3,4,1,2,4,3,2,1]).reshape((4,4))
    ves = vestiginum(arr=seq3)
    ves.print_matrix()
    ves.trace()

