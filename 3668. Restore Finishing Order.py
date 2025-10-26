order = [1,4,5,3,2]
friends = [2,5]

# Output: [5,2]
ansList = []
for i in range(len(order)):
    if order[i] in friends:
        ansList.append(order[i])
    
print(ansList) 