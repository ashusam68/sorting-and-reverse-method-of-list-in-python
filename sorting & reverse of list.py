# SORTING
a = []
l = int(input("enter length of the list : "))
print("enter element : ")
for i in range(l):
    s = int(input())
    a.append(s)
print('list is : ', a)
for i in range(l):
    for j in range(l-1):
        if( (a[l-j-1]) < (a[l-j-2]) ):
            a[l-j-1], a[l-j-2] = a[l-j-2], a[l-j-1]
print('after sorting : ', a)

# # REVERSE
# a, b = [], []
# l = int(input('enter the length of the list : '))
# print('enter element :  ', end='')
# for i in range(l):
#     c = int(input())
#     a.append(c)
# print('list is : ', a)
# for i in range(l):
#     b.append(a[l-i-1])
# print('Reverse list is : ', b)