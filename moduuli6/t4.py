# This program calculates the sum of the numbers in the userList using a function

userList = [24, 26, 5, 10, 35]


def list_sum(user_list):
    sum_of_list = int(0)
    for i in user_list:
        sum_of_list += i
    return sum_of_list


print("The sum of the numbers in list is " + str(list_sum(userList)))
