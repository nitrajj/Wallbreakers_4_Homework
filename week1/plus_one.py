def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] +=1
        for i in range(len(digits)-1,0,-1):
            if digits[i] != 10:
                break
            digits[i]=0
            digits[i-1] +=1
        print(digits)
        
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits

digits = [1,2,3]
plusOne(digits)