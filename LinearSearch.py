# complexity of linear search
# is O(n)

def linearsearch(lst, key):
    for position in range(0,len(lst)) :
        if lst[position] == key :
            return position
            break
        else:
            continue
    

lst = []
lenght = int(input('Enter the no. of items :'))
for i in range(0,lenght):
    element = int(input())
    lst.append(element)

key = int(input('Enter the item you want to search :'))

result = linearsearch(lst,key)
if result == None:
    print('Item Not Found')
else:
    print('Item Found at index :',result)
