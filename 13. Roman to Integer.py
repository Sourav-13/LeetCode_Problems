class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900,
                        }
        valid_pairs = {
            'I': ('V', 'X'),
            'X': ('L', 'C'),
            'C': ('D', 'M')
                        }
        num = 0
        flag = 0
        l_idx = len(s) -1
        for i,ch in enumerate(s):
            if flag:
                flag = 0
                continue
            # if (ch == 'I' and i!=l_idx and s[i+1] in ('V', 'X')) \
            # or (ch == 'X' and i!=l_idx and s[i+1] in ('L', 'C')) \
            # or (ch == 'C' and i!=l_idx and s[i+1] in ('D', 'M')):
            if i != l_idx and ch in valid_pairs and s[i+1] in valid_pairs[ch]:
                num += roman_dict[s[i]+s[i+1]]
                flag = 1
            else:
                num += roman_dict[ch]
        return num
    
#best
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        
        for i in range(len(s) - 1):
            current_val = roman_map[s[i]]
            next_val = roman_map[s[i+1]]
            if current_val < next_val:
                total -= current_val
            else:
                total += current_val
        total += roman_map[s[-1]]
        
        return total