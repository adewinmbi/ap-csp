def swap(list, i, j): # i and j are the two indices that must be swapped
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def partition(list, low, high):
    pivot = list[high]
    i = (low - 1)

    for j in range(low, high):
        if (list[j] < pivot):
            i += 1
            swap(list, i, j)
    
    swap(list, i + 1, high)
    return (i + 1)

def sort(list, start, end):
    if (start < end):
        part = partition(list, start, end)

        # Elements before and after partition
        sort(list, start, part - 1)
        sort(list, part + 1, end)

my_list = [10, 7, 8, 9, 1, 5]
sort(my_list, 0, len(my_list) - 1)

print(my_list)