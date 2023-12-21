#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: December 20, 2023
# This program display the average of the user's marks


def calc_average(list_of_int):
    # initialize sum to 0
    sum = 0

    # use a for each loop when a_num is in list_of_int
    for a_num in list_of_int:
        # set sum to marks a_num + sum
        sum += a_num

    # calculate average
    average = sum / len(list_of_int)

    # return average
    return average


def main():
    # declare marks_list
    marks_list = []

    # tell the user what the program does
    print("This program display the average of the following marks :")

    # use a do while loop when user_mark is not -1
    while True:
        # get user mark
        user_mark_str = input("Enter your mark here (type stop to exit):")
        try:
            # covert user mark to float
            user_mark_float = float(user_mark_str)

            # if user mark is > 100 or < -1, tell the user it is invalid
            if user_mark_float < -1 or user_mark_float > 100:
                print("{} is not a number between 0 and 100.".format(user_mark_float))

            # append user mark  to marks_list
            marks_list.append(user_mark_float)
        except:
            # if user mark cannot be converted, tell the user to enter a valid number
            print("{} is not valid, please enter a valid number.".format(user_mark_str))
        if user_mark_str == "-1":
            # eliminate that last element of marks list
            marks_list.pop()

            # call the calc_average function
            average = calc_average(marks_list)

            # display the average
            print("The average of your marks is {} %.".format(average))

            # break out of the loop
            break


if __name__ == "__main__":
    main()
