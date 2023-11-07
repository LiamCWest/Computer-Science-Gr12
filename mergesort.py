def mergesort(list):
    if(len(list) > 1):
        split = len(list)//2
        bottom = mergesort(list[split:])
        top = mergesort(list[:split])
        return merge(bottom, top)
    else:
        return list
    
def merge(list1, list2):
    merged = []
    while (len(list1) > 0 and len(list2) > 0):
        if(list1[0] <= list2[0]):
            merged.append(list1[0])
            list1.pop(0)
        else:
            merged.append(list2[0])
            list2.pop(0)

    if(len(list1) > 0):
        merged += list1
    elif(len(list2) > 0):
        merged += list2
            
    return merged

list = [6,3,7,2,9,5,0,3,7]
print(mergesort(list))