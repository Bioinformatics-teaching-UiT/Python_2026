animals = ["dog","cat","mouse","dog"]

for i in range (0,len(animals),2):
    print(animals[i])

for animal in animals:
    if animal == "dog":
        animals.remove(animal)

print(animals)