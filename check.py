# print(name:=input())

# num = [1, 2, 3, 4, 5]
# for i in range(len(num)):
#     print(num[i])
    
# a, b = 0, 1
# while a < 10:
#     print(a, end=" ")
#     a, b = b, a+b
    # print(a +" "+ b) error
    # print(f"{a} {b}")

# words = ['cat', 'window', 'defenestrate']
# for i in words:
#     print(i, len(i))
# print()

# num = [1, 2, 3, 4, 5]
# for i in range(len(num)):
#     print(f"{num[i]} {i}")
    
    
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        
for user in active_users:
    print(user)