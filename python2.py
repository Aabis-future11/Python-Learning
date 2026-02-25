#PART-2:PYTHON DATA STRUCTURES, EXECPTION HANDLING & FILE HANDLING
#QUESTION SET 1: Questions on List:
# Print positive and negative elements of an List?
a=[]
n=int(input("enter no of elements:"))
for i in range(n):
    x=int(input("enter number:"))
    a.append(x)
print("#-----positive numbers-----#")
for i in a:
    if i>0:
        print(i)
print("#-----negative numbers------#")
for j in a:
    if j<0:
        print(j)
# Mean of List elements?
a=[12,89,-9,67,88,77,34,12,22,67,89]
sum=0
for i in a:
    sum+=i
mean=sum/11
print(f"the mean is {mean}")

# Find the greatest element and print its index too?
a=[12,34,-45,78,90,789,56,44,123,456,29]
greatest=a[0]
for i in range(len(a)):
    if a[i]>greatest:
        greatest=a[i]
print("the greatest number is:",greatest)

# Find the second greatest element?
a=[12,34,-45,78,90,789,56,44,123,456,29]
a.sort()
greatest=a[0]
sec_greatest=a[0]
for i in range(len(a)):
    if a[i]>greatest:
       sec_greatest=greatest
       greatest=a[i]
print(f"the greatest element is {greatest} and second greatest is {sec_greatest}")

# Check if List is sorted or not.
a=[]
n=int(input("enter no of numbers:"))
for i in range(n):
    x=int(input("enter number:"))
    a.append(x)

for i in range(len(a)-1):
    if a[i+1]>a[i]:
        continue
    else:
        print("list is not sorted")
        break
else:
    print("list is sorted")
a.sort()
print("the sorted list is:",a)
#QUESTION SET 2: Questions on Dictionary:
# Write a Python script to merge two Python dictionaries?
a={1:23,2:45,3:67,4:89,5:77}
b={6:88,7:45,8:100,9:200,10:234}
for i in b:
    a[i]=b[i]
print(a)
# Write a Python program to sum all the values in a dictionary?
a={1:89,2:454,3:56,4:44,5:88}
sum=0
for i in a:
    sum+=a[i]
print(sum)
# Count the frequency of each element?
a=[1,1,1,1,2,2,3,3,3,3,4,5,6,7,7,7,7,7]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
# Write a Python program to combine two dictionary by adding values for common keys.
a={1:89,2:56,3:90,4:45,5:99}
b={5:78,6:88,4:45,8:99,9:102}
for i in b:
    if i in a.keys():
        a[i]+=b[i]
    else:
        a[i]=b[i]
print(a)



