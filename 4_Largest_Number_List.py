x = []
list1 = []
n = int(input("Number of elements in list:"))

for i in range(0,n):
    print("Enter the", i, "number:")
    a = int(input()) 
    x.append(a)
print()
print("Created list based on user inputs:",x)
print()
list1 = x
list1.sort()
print("Sorted list:")
print(list1)
print()
print("Maximum Number in the list is:",list1[-1])

