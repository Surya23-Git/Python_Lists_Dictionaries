x = []
n = int(input("Number of elements in list:"))

for i in range(0,n):
    print("Enter the", i, "number:")
    a = int(input()) 
    x.append(a)

avg = sum(x)/(len(x))

print("Average of the numbers in the list:",avg)






