import random

throws = []

for i in range(7):
    throws.append(random.randint(1, 6))

print("Original throws:", throws)

random.shuffle(throws)
print("Shuffled throws:", throws)

throws.sort(reverse=True)
print("Descending order:", throws)

for i in range(1, 7):
    print(i, "appeared", throws.count(i), "times")
