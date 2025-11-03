from collections import defaultdict

s = "bananas"
anana

# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

char_dict = defaultdict(int)
for ch in s:
    char_dict[ch] += 1
    
total_count = 0
flag = 0
# if len(my_dict) == 1:
    

for val in char_dict.values():
    if val%2 == 0:
        total_count += val
    else: 
        flag = 1
    
    

print(total_count+flag)