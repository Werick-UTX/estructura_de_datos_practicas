calif = [5,10,8,9,7,6,10,5,6,7,8,9,4,7,8,5,2,7,5]
n = len(calif)
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):
        if calif[i]>calif[i+1]:
            calif[i],calif[i+1] = calif[i+1],calif[i]
            swapped = True
print("Orden acendente: ",calif)
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):
        if calif[i] < calif[i+1]:
            calif[i],calif[i+1] = calif[i+1],calif[i]
            swapped = True
print("Orden descendente: ",calif)