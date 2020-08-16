#加一
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lenth = len(digits)
        i = lenth-1
        while i>=0:
            digits[i]+=1
            digits[i] = digits[i] % 10
            if digits[i] != 0:
                return digits
            i-=1
        digits.append(0)
        digits[0] =1
        return digits