#Selection_Sort
def selection_sort(list_a):
    index_length = range(0,len(list_a))
    
    for i in index_length:
        minium_value = i

        for j in range(i+1,len(list_a)):
            if list_a[j] < list_a[minium_value]:
                minium_value = j
        if minium_value != i:
            list_a[minium_value],list_a[i]=list_a[i],list_a[minium_value]
    return list_a

print(selection_sort([1,4,7,8,5,2,3,6,9]))