list1 = []
num = int(input("How many numbers do you want to enter?: "))

print("Enter the numbers one by one:")

for k in range(num):
    list1.append(int(input()))

print("The unsorted list is: ",list1)

for j in range(len(list1)-1,0,-1):
    swapped = False
    for i in range(j):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
            swapped = True
    if not swapped:
        break
print("The sorted list is: ", list1)