# modifiedList will have get originalList's numbers excluding odd numbers

originalList = [2, 3, 4, 5, 6, 7, 8]
modifiedList = []


def modify_list(original_list, modified_list):
    for i in original_list:
        if i % 2 == 0:
            modified_list.append(i)
    return modified_list


print("Original list: " + str(originalList) + "\nModified list: " + str(modify_list(originalList, modifiedList)))
