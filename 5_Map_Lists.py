#list1 = [1,2,3,4,5]
#list2 = [6,7,8,9,10]
print("Number of elements in the list1 and list2 should be same")
print()
list1 = []
n = int(input("Number of elements in list1:"))
for i in range(0,n):
    print("Enter the", i, "number:")
    a = int(input()) 
    list1.append(a)
print("-----")
list2 = []
m = int(input("Number of elements in list1:"))
for i in range(0,m):
    print("Enter the", i, "number:")
    b = int(input()) 
    list2.append(b)

dictionary = dict(zip(list1,list2))

print(dictionary)






