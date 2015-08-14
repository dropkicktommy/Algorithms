################################################################################
############################### INSERTION SORT ####################### O(n^2) ##
################################################################################
def insertion_sort(x):
    # convert input to list
    x = list(x)
    # iterate thru every item in list
    for i in range(1, len(x)):
        # set index to match current item in list
        j = i
        # compare current item to value at index
        while j > 0 and x[j] < x[j - 1]:
            # swap if item is less than value at index
            x[j], x[j - 1] = x[j - 1], x[j]
            # move index one step backward in list
            j -= 1
        # move to next item in list
        i += 1
    return x
    
################################################################################
############################### SELECTION SORT ####################### O(n^2) ##
################################################################################
def selection_sort(x):
    # convert input to list
    x = list(x)
    # iterate thru every item in list
    for i in range(0, len(x) - 1):
        # initialize minimum value to current item
        j_min = i
        # index thru remaining items in list
        for j in range(i + 1, len(x)):
            # compare value at index to minimum value
            if x[j] < x[j_min]:
                # set new minimum value if found
                j_min = j
            # move index one step forward in list
            j += 1
        # compare minimum value to current item
        if j_min != i:
            # swap if item is not the minimum
            x[i], x[j_min] = x[j_min], x[i]
        # move to next item in list
        i += 1
    return x