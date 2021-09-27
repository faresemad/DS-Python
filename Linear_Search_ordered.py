#Linear_Search_Ordered
def orderd_linear_search(sequance,item):
    position = 0
    found = False
    stop = False
    index = -1
    while position < len(sequance) and not found and not stop:
        if sequance[position] == item :
            found = True
            index = position
        else:
            if sequance[position] >item:
                stop = True
            else:
                position = position +1
    return found , index

sequance_a=[1,4,2,5,3,6,7,8,9]
print(orderd_linear_search(sequance_a,11))