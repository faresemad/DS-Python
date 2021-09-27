#Bubble_Sort
def bubble_sort(list_a):
    index_length = len(list_a) -1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a

print(bubble_sort([2,5,8,4,1,9,6,3,7]))