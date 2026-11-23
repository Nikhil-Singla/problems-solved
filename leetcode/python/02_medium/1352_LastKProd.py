class ProductOfNumbers:

    def __init__(self):
        self.prod = [1]

    def add(self, num: int) -> None:
        element = self.prod[-1]
        
        if num == 0:
            self.prod = [0] * (len(self.prod)) + [1]    
            # From a zero on, everything before this now includes 0 in the last k elements, so will always be 0
            
        else:
            element *= num
            self.prod.append(element)

    def getProduct(self, k: int) -> int:
        back = self.prod[-k-1]

        return 0 if back <= 0 else self.prod[-1]//back

        # if furthest == 0:
        #     return 0
        # else:
        #     return latest//furthest
