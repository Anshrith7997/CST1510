import random

friends = ["Alice", "Bob", "Charlie", "Dana", "Ella"]

num_friends = len(friends)
index = random.randint(0, num_friends - 1)
payer = friends[index]

print(f"{payer} is paying the bill today!")