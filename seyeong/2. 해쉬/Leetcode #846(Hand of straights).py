class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        length = len(hand)
        
        if length % W != 0:
            return False
        
        
        c = collections.Counter(hand)
        
        for i in range(min(hand), max(hand)+1):
                 
            if c[i] > 0:
                temp = c[i]
                
                for j in range(W):
                    
                    
                    if c[i+j] >= temp:
                        
                        c[i+j] -= temp
                    else:
                        
                        return False

        return True