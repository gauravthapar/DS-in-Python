# Time Complexity of Binary Search
# is O(log(n))

def binarysearch(lst, key) :
    low = 0
    high = len(lst) -1 
    while low <= high :
        mid = (low+high)//2
        if key == lst[mid] :
            return mid
        elif key < lst[mid] :
            high = mid - 1
        else :
            low = mid + 1
    else:
        return False


lst = []
lenght = int(input('Enter the number of elements you want to enter : '))
for i in range(0,lenght) :
    element = int(input())
    lst.append(element)

lst.sort()

key = int(input('Enter the item you want to search :'))

result = binarysearch(lst, key)

if result == False :
    print('Item Not Found')
else :
    print('Item Found at index :', result)