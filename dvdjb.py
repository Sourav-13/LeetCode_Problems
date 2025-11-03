# nums = [-4,-1,0,2,3,10]
nums = [-1,-2]

# Output: [0,1,9,16,100]
# Output: [4,9,9,121]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# num_squared = [num*num for num in nums]
# num_squared.sort()
neg_list = []
ans_list = []

for val in nums:
    if val <0:
        neg_list.append(val)
    else:
        if neg_list:
            neg_val = -neg_list[-1]
            if neg_val <= val:
                ans_list.append(neg_val*neg_val)
                neg_list.pop()
                ans_list.append(val*val)
            else:
                ans_list.append(val*val)
        else:
            ans_list.append(val*val)
    
    