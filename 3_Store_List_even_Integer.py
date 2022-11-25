x = []
n = int(input("Number of elements in list:"))

for i in range(0,n):
    print("Enter the", i, "number:")
    a = int(input())
    if ((a%2)==0):
        x.append(a)
avg = sum(x)/(len(x))
print("Stored Even values in the list are:\n",x)
print()
print("Average of the numbers in the list:",avg)





