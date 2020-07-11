def find_median(list1, list2):
    if len(list2)>len(list1):
        return find_median(list2,list1)

    length1 = len(list1)
    length2 = len(list2)
    if length1 % 2 == 1:
        mid_1 = list1[((length1 - 1) / 2)]
    if length1 % 2 == 0:
        mid_1 = list1([length1 / 2]+list1[length1 / 2-1]) / 2

    if length2 % 2 == 1:
        mid_2 = list2[((length2 - 1) / 2)]
        t =
    if length2 % 2 == 0:
        mid_2 = list2([length2 / 2]+list2[length2 / 2-1]) / 2

    if mid_1 >= mid_2:
        find_median(list1,list2[:])