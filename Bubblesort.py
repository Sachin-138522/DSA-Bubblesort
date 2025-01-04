# Sort array using Bubble sort
Array = [55, 334, 53, 3434, 55, 3, 56, 66, 33 ,44, 656, 334,55343 ,66343, 53353, 5366]
n = len(Array)
for i in range (n-1):
    swapped = False
    for j in range (n-i-1):
        if Array[j]> Array[j+1]:
            Array[j],Array[j+1] = Array[j+1] , Array[j]
        swapped = True
    if not swapped :
        break
print("Sorted Array is :" , Array)