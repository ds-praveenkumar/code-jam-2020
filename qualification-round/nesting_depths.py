#  nesting_depths.py

class nesting_depths:

    def __init__(self, digits=str):
        self.seq = None
        self.digits = digits

    def nesting_depths(self, ):
        
        s_ = []
        previous_digits = 0
        for val in str(self.digits): 
            val = int(val)         
            if val != 0:
                s_.append('('*val)
                s_.append(str(val))
                s_.append(')'* val)
                previous_digits = val
            else:
                s_.append(str(val))
                previous_digits = val
            
        s_ = "".join(s_)
        print(s_)


if __name__ == "__main__":
    digits_input = [ "101", "0000", "111000", "1"]
    for items in  digits_input:
        nd = nesting_depths(digits=items)
        nd.nesting_depths()
