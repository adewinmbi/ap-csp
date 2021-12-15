# Brianna Adewinmbi
# Period 5
# Quiz with Lists

''' This is an individual effort!  

	Write a program that will demonstrate the following:
    1. merge the three list into one list
	2. remove any repeated numbers in the new list
	3. sort the new list from highest to lowest
	4. Print the new list as a string
	5. Comment out your code
'''

# ===== Initial Lists =====
my_list1 = [11001011, 11001021, 11001031, 11001041, 11001051, 11001061, 11001071, 11001081, 11001091, 11001101, 11001111, 11001121, 11001131, 11001141, 11001451, 11001151, 11001161, 11001171, 11001181]
my_list2 = [11001021, 11001121, 11001481, 11001141, 11001151, 11001161, 11001491, 11001501, 11001191, 11001201, 11001211, 11001221, 11001231, 11001241, 11001251, 11001261, 11001471, 11001271, 11001281]
my_list3 = [11001291, 111001311, 11001321, 11001331, 11001341, 11001351, 11001261, 11001361, 11001371, 11001271, 11001381, 11001391, 11001401, 11001411, 11001421, 11001141, 11001431, 11001441]

new_list = []

# Merge lists here. Store them in a new list. Remove duplicates from the list.

def merge_with_new_list(list):
	for i in list:
		if i not in new_list: # Prevent duplicates from being added in the first place
			new_list.append(i)

# Merge all lists
merge_with_new_list(my_list1)
merge_with_new_list(my_list2)
merge_with_new_list(my_list3)

# ===== Sort list from highest to lowest =====
# The Quicksort sorting algorithm was implemented 

def swap(list, i, j): # i and j are the two indices that must be swapped
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def partition(list, low, high):
    pivot = list[high]
    i = (low - 1)

    for j in range(low, high):
        if (list[j] > pivot): # Just change this operator to change from sorting lowest --> highest to highest --> lowest
            i += 1
            swap(list, i, j)
    
    swap(list, i + 1, high)
    return (i + 1)

def sort(list, start, end):
    if (start < end):
        part = partition(list, start, end)

        # Sort elements before and after partition
        sort(list, start, part - 1)
        sort(list, part + 1, end)

sort(new_list, 0, len(new_list) - 1)

# Extra method: Check if there are duplicates in the list
def check_duplicates(list):
	for i in range(len(list) - 1):
		if list[i] == list[i + 1]:
			print("Duplicate detected!") # This should not print if duplicates were removed correctly

check_duplicates(new_list)

# ===== Print New List =====

print(new_list)
