def linearsearch(l,n,key):
    for i in range(0,n):
        if(l[i]==key):
            return i
    return -1    
n=int(input("enter no.of elements to insert:"))
l=[]
for i in range(0,n):
    ele=int(input("enter the elements:"))
    l.append(ele)
print(l)
print("enter the key value:")
key=int(input("enter the value to search:"))
result=linearsearch(l,n,key)
if result==-1:
    print("element is not found")
else:
    print("element is found:",result)
  