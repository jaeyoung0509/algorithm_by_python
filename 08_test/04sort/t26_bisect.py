from bisect import bisect_left ,bisect_right

def count_by_value(array , left_vlaue , right_value):
    right_indx = bisect_right(array ,right_value)
    left_index = bisect_left(array , left_vlaue)
    return right_indx - left_index


array= [1 , 1, 2 ,2 , 2 , 3]
count = count_by_value(array , 2, 2)
print(count)