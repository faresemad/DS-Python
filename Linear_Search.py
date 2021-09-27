#Linear_Search
def linear_search(sequance,item):
    position = 0
    found = False
    index = -1
    while position < len(sequance) and not found:
        if sequance[position] == item :
            found = True
            index = position
        else:
            position = position + 1
    return found , index

sequance_a=[1,4,2,5,3,6,7,8,9]
print(linear_search(sequance_a,8))