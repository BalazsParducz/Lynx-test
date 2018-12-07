table = [[1, 5, 7, 10], [3, 13, 14, 15], [6, 16, 19, 25]]
larger_values = []


def array_walk(list_length, list_of_lists_length):
    # get the max number of iterations
    top = list_length
    if list_length >= list_of_lists_length:
        top = list_of_lists_length
    i = 0
    j = 0
    # add value at top left corner of the table
    larger_values.append(table[i][j])
    # start iteration through the table
    for k in range(0, top):
        # move one down in table if that value is bigger
        if table[i][j + 1] < table[i + 1][j]:
            larger_values.append(table[i + 1][j])
            i += 1
            # move to the right after reaching the last element
            if i == list_length-1:
                while j < list_of_lists_length:
                    larger_values.append(table[i][j])
                    j += 1
        # move one right in table if that value is bigger
        else:
            larger_values.append(table[i][j + 1])
            j += 1
            # move down after reaching
            if j == list_of_lists_length-1:
                while i < list_length:
                    larger_values.append(table[i][j])
                    i += 1
    # print all numbers without duplicates
    print(list(set(larger_values)))
    # print their sum
    print(sum(set(larger_values)))


array_walk(len(table), len(table[0]))
