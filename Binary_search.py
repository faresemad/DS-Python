#Binary_Search
def binary_search(sequance,item):
    begin_index = 0
    end_index = len(sequance)-1
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) //2
        midpoint_value = sequance[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint -1
        else:
            begin_index = midpoint +1
    return None

sequance_a=[1,4,2,5,3,6,7,8,9]
print(binary_search(sequance_a,1))