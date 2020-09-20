# parenting_partnering

"""
functions
1. detect Over lap
2. edge cases:
    * no over lap
    * overlap but can be distributed
    * no possible slots available
    [1,12,43,4,5,6]

"""

class ParentingPartenering:

    def __init__(self):
        pass

    
    def parenting_partnering(self, slots):
        slots_len = len(slots)
        possiblity_mat = []
        # case 1 no overlap
        for val1, val2 in zip(slots[1:], slots[2:]):
            if val1 <= val2:
                possiblity_mat.append(1)
            elif val1 > val2:
                possiblity_mat.append(0)
        print(possiblity_mat)

            


if __name__ == "__main__":
    slot1 = [1,40,4,6]

    pp = ParentingPartenering()
    pp.parenting_partnering(slot1)

                
